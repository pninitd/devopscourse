from flask import Flask, request

app = Flask(__name__)

# local users storage
users = {'1': 'daniel', '2': 'ppp', '3': 'ddd'}

# supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        return {'user_id': user_id, 'user_name': users[user_id]}, 200 # status code

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        return {'user id': user_id , 'user name': user_name, 'status': 'saved'}, 200 # status code


app.run(host='127.0.0.1', debug=True, port=5000)