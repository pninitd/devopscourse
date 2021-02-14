import json

from flask import Flask, request, jsonify

# for some reason its running all the prints in lesson5_ex_db.py so you can comment out... any idea why?
from lesson5_jan31.lesson5_ex_db import print_all_as_json, insert_dogs

app = Flask(__name__)

# http://127.0.0.1:5000/dogs
@app.route('/dogs')
def dogs():
    results = print_all_as_json()
    jsonResult = json.loads(results)
    return jsonify(jsonResult), 200


# http://127.0.0.1:5000/add_dog
# body: {"name": "rexi", "age":2, "breed": "husky"}
@app.route('/add_dog', methods=['POST'])
def add_dog():
    # getting the json data payload from request
    request_data = request.json
    # treating request_data as a dictionary to get a specific value from key
    name = request_data.get('name')
    age = request_data.get('age')
    breed = request_data.get('breed')
    success = insert_dogs(name, age, breed)
    if success:
        return {'name': name, 'age': age, 'breed': breed, 'status': 'saved'}, 201
    else:
        # TODO: errors should be handled better for all types of errors
        return {'name': name, 'age': age, 'breed': breed, 'status': 'error'}, 400


app.run(host='127.0.0.1', debug=True, port=5000)