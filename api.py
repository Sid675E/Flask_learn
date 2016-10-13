from flask import Flask, request, jsonify, json, render_template, request, redirect, url_for
from flask_restful import Resource, Api
from dataFlask import Base, data_Flask

app = Flask(__name__)
api = Api(app)


class TodoSimple(Resource):
	def get(self):
		#return jsonify(data_Flask=[i.serialize for i in items])

	def put(self,iid):
		return "JSON Message: "

api.add_resource(TodoSimple, '/testing/<int:iid>')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)