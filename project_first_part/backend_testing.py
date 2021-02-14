import requests
from project_first_part.db_connector import get_user_name_by_id

# This backend test will:
# 1. Post a new user data to the REST API using POST method.
# 2. Submit a GET request to make sure status code is 200 and data equals to the posted data.
# 3. Check posted data was stored inside DB (users table).


def check_new_user_creation(user_id, user_name):
    success = False
    try:
        # create a new user
        res = requests.post("http://127.0.0.1:5000/users/" + str(user_id), json={'user_name': user_name})
        print("insert new user: ", res.json())
        assert res.ok
        data = res.json()
        # check json result from the call, user created successfully
        assert data['user_added'] == user_name
        assert data['status'] == 'ok'
        assert res.status_code == 201
        success = True
    except requests.exceptions.ConnectionError as e:
        print("Connection refused ", e)
    finally:
        return success


def check_get_user(user_id, user_name):
    success = False
    try:
        # check results from get api
        res = requests.get("http://127.0.0.1:5000/users/" + str(user_id))
        print('get user: ', res.json())
        assert res.ok
        data = res.json()
        # check json result from the call
        assert data['user_name'] == user_name
        assert data['status'] == 'ok'
        assert res.status_code == 200
        success = True
    except requests.exceptions.ConnectionError as e:
        print("Connection refused ", e)
    finally:
        return success


def check_user_in_db(user_id, user_name):
    # check directly in DB that we have the new user
    user_name_from_db = get_user_name_by_id(user_id)
    if user_name_from_db != user_name or user_name_from_db == '':
        raise Exception("test failed")
    print('new user %s returned from db' % user_name_from_db)
    return user_name_from_db


def main():
    # Test params:
    user_id = 6
    user_name = 'john'

    try:
        # 1. create a new user
        success = check_new_user_creation(user_id, user_name)
        if success:
            # 2. check results from get api
            check_get_user(user_id, user_name)

            # 3. check directly in DB that we have the new user
            check_user_in_db(user_id, user_name)
        else:
            raise Exception("test failed")
    finally:
        print("backend test ended")


if __name__ == '__main__':
    main()
