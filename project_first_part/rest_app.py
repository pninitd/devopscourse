from flask import Flask, request
from project_first_part.db_connector import get_user_name_by_id, is_id_exist, create_user, update_user_by_id, \
    delete_user_by_id

app = Flask(__name__)


# http://127.0.0.1:5000/users/<user_id>
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            # check if id exist in db
            if is_id_exist(user_id):
                # id exist
                user_name = get_user_name_by_id(user_id)
                if user_name != '':
                    # check no error returned from backend
                    return {'status': 'ok', 'user_name': user_name}, 200
                else:
                    return {'status': 'error',
                            'reason': 'failed to get user' + user_id + ', general error'}, 500
            else:
                return {'status': 'error', 'reason': 'no such id'}, 500
        except Exception as e:
            return {'status': 'error',
                    'reason': 'failed to get user' + user_id + ', general error'}, 500

    elif request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a user_name value from key
            user_name = request_data.get('user_name')
            # check if id already exist in db
            if is_id_exist(user_id):
                return {'status': 'error', 'reason': 'id ' + user_id + ' already exists'}, 500
            else:
                success = create_user(user_id, user_name)
                if success:
                    return {'status': 'ok', 'user_added': user_name}, 201
                else:
                    return {'status': 'error',
                            'reason': 'failed to save' + user_id + ', general error'}, 500
        except Exception as e:
            return {'status': 'error',
                    'reason': 'failed to save' + user_id + ', general error'}, 500

    elif request.method == 'PUT':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a user_name value from key
            user_name = request_data.get('user_name')
            # check if id exist in db
            if is_id_exist(user_id):
                # id exist
                success = update_user_by_id(user_id, user_name)
                if success:
                    return {'status': 'ok', 'user_updated': user_name}, 200
                else:
                    return {'status': 'error',
                            'reason': 'failed to update user ' + user_id + ', general error'}, 500
            else:
                return {'status': 'error', 'reason': 'no such id'}, 500
        except Exception as e:
            return {'status': 'error',
                    'reason': 'failed to update user ' + user_id + ', general error'}, 500

    elif request.method == 'DELETE':
        try:
            # check if id exist in db
            if is_id_exist(user_id):
                # id exist
                success = delete_user_by_id(user_id)
                if success:
                    return {'status': 'ok', 'user_deleted': user_id}, 200
                else:
                    return {'status': 'error',
                            'reason': 'failed to delete user ' + user_id + ', general error'}, 500
            else:
                return {'status': 'error', 'reason': 'no such id'}, 500
        except Exception as e:
            return {'status': 'error',
                    'reason': 'failed to delete user ' + user_id + ', general error'}, 500


app.run(host='127.0.0.1', debug=True, port=5000)
