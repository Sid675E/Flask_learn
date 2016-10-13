from flask import Flask, render_template, request, redirect, jsonify, json, abort,g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataFlask import Base, data_Flask,User

from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

engine = create_engine('postgresql+psycopg2://postgres:XxxAahSn@2*5@localhost/restr')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@auth.verify_password
def verify_password(username_or_token, password):
    #Try to see if it's a token first
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(id = user_id).one()
    else:
        user = session.query(User).filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True



@app.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })

@app.route('/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        #print "missing arguments"
        abort(400) 
        
    if session.query(User).filter_by(username = username).first() is not None:
        #print "existing user"
        user = session.query(User).filter_by(username=username).first()
        return jsonify({'message':'user already exists'}), 200#, {'Location': url_for('get_user', id = user.id, _external = True)}
        
    user = User(username = username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({ 'username': user.username }), 201#, {'Location': url_for('get_user', id = user.id, _external = True)}


############################ get, post and delete for accessing data in database ##########################

@app.route('/firstt')
def dataJSON_get():
    items = session.query(data_Flask).all()
    return jsonify(data_Flask=[i.serialize for i in items])

@app.route('/firstt/new', methods = ['GET', 'POST'])
def dataJSON_post():
    if request.method == 'GET':
    # RETURN ALL DATA IN DATABASE
        item = session.query(data_Flask).all()
        return jsonify(data_Flask=[i.serialize for i in item])

    elif request.method == 'POST':
    # MAKE A NEW DATA COLUMN AND STORE IT IN DATABASE
        #if request.headers['Content-Type'] == 'application/json':
        data_item = data_Flask(name = request.json["name"], description = request.json["description"])
        session.add(data_item)
        session.commit()
        item = session.query(data_Flask).all() 
        return jsonify(data_Flask=[i.serialize for i in item]) 

@app.route('/firstt/delete/<int:iD>', methods = ['DELETE'])
def dataJSON_delete(iD):
    if request.method == 'GET':
    # RETURN ALL DATA IN DATABASE
        #item = session.query(data_Flask).all()
        #return jsonify(data_Flask=[i.serialize for i in item])
        return "get is here"

    if request.method == 'DELETE':
    # DELETE DATA COLUMN IN DATABASE
        dflask = session.query(data_Flask).filter_by(id = iD).one()
        #if len(dflask) == 0:
            #abort(404)
        session.delete(dflask)
        session.commit()

        item = session.query(data_Flask).all() 
        return jsonify(data_Flask=[i.serialize for i in item])     


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)