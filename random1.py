@app.route('/restaurants/<int:restaurant_id>/new', methods = ['GET', 'POST'])
def all_restaurants_handler():
  if request.method == 'GET':
    # RETURN ALL RESTAURANTS IN DATABASE
    restaurants = session.query(Restaurant).all()
    return jsonify(restaurants = [i.serialize for i in restaurants])

  elif request.method == 'POST':
    # MAKE A NEW RESTAURANT AND STORE IT IN DATABASE
    if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    if not request.json or not 'title' in request.json:
        abort(400)

    restaurants = {
        'id': new[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    restaurants.append(task)
    return jsonify({'task': task}), 201


    location = request.args.get('location', '')
    mealType = request.args.get('mealType', '')
    restaurant_info = findARestaurant(mealType, location)
    if restaurant_info != "No Restaurants Found":
      restaurant = Restaurant(restaurant_name = unicode(restaurant_info['name']), restaurant_address = unicode(restaurant_info['address']), restaurant_image = restaurant_info['image'])
      session.add(restaurant)
      session.commit() 
      return jsonify(restaurant = restaurant.serialize)
    else:
      return jsonify({"error":"No Restaurants Found for %s in %s" % (mealType, location)})
    
@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
  restaurant = session.query(Restaurant).filter_by(id = id).one()
  if request.method == 'GET':
    #RETURN A SPECIFIC RESTAURANT
    return jsonify(restaurant = restaurant.serialize)
  elif request.method == 'PUT':
    #UPDATE A SPECIFIC RESTAURANT
    address = request.args.get('address')
    image = request.args.get('image')
    name = request.args.get('name')
    if address:
        restaurant.restaurant_address = address
    if image:
        restaurant.restaurant_image = image
    if name:
        restaurant.restaurant_name = name
    session.commit()
    return jsonify(restaurant = restaurant.serialize)

  elif request.method == 'DELETE':
    #DELETE A SPECFIC RESTAURANT
    session.delete(restaurant)
    session.commit()
    return "Restaurant Deleted"


    todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}