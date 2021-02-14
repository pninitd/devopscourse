import json
from werkzeug.exceptions import HTTPException, InternalServerError
from flask import Flask
from project_first_part.db_connector import is_id_exist, get_user_name_by_id

app = Flask(__name__)


# http://127.0.0.1:5001/users/get_user_data/<user_id>
@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    # check if id exist in db
    if is_id_exist(user_id):
        # id exist
        user_name = get_user_name_by_id(user_id)
        if user_name != '':
            # check no error returned from backend
            return "<H1 id='user'>" + user_name + "</H1>", 200
        else:
            return "<H1 id='error'> error getting results from db </H1>", 500
    else:
        return "<H1 id='error'> no such user: " + user_id + "</H1>", 500


# I tried few error handlers
@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return "<H1 id='error'> error getting results from db </H1>", 500


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(InternalServerError)
def handle_500(e):
    return "<H1 id='error'> error getting results from db </H1>", 500


app.run(host='127.0.0.1', debug=True, port=5001)