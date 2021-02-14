import pymysql
from datetime import datetime

# DataGrip ddl:
# create table users
# (
# 	user_id int not null
# 		primary key,
# 	user_name varchar(50) not null,
# 	creation_date varchar(50) null
# );


def open_connection():
    user = 'QzeMAiiWP6'
    password = 'r8Dopb5X8y'
    dbname = 'QzeMAiiWP6'
    schema = 'QzeMAiiWP6'
    host = 'remotemysql.com'
    port = 3306

    # Establishing a connection to DB
    db_con = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, cursorclass=pymysql.cursors.DictCursor)
    db_con.autocommit(True)
    return db_con


def querydb(sql):
    db_con = open_connection()

    # Getting a cursor from Database
    cursor = db_con.cursor()

    # Getting all data from table “users”
    cursor.execute(sql)
    db_con.close()
    return cursor


# function will create a new user and return TRUE if success
def create_user(user_id, name):
    is_success = False
    try:
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # print("date and time =", dt_string)
        sql = "INSERT into QzeMAiiWP6.users (user_id, user_name, creation_date) VALUES (%s, '%s', '%s');" % (user_id, name, dt_string)
        cursor = querydb(sql)
        if cursor.rowcount > 0:
            is_success = True
    except Exception as e:
        print("general error when trying to create new user in DB ", e)
    finally:
        cursor.close()
        return is_success


# function will update a specific user and return TRUE if success
def update_user_by_id(user_id, name):
    is_success = False
    try:
        sql = "UPDATE QzeMAiiWP6.users SET user_name = '%s' WHERE user_id =%s;" % (name, user_id)
        cursor = querydb(sql)
        if cursor.rowcount > 0:
            is_success = True
    except Exception as e:
        print("general error when trying to update user in DB ", e)
    finally:
        cursor.close()
        return is_success


# function will delete a specific user and return TRUE if success
def delete_user_by_id(user_id):
    is_success = False
    try:
        sql = "DELETE FROM QzeMAiiWP6.users WHERE user_id =%s;" % user_id
        cursor = querydb(sql)
        if cursor.rowcount > 0:
            is_success = True
    except Exception as e:
        print("general error when trying to delete user in DB ", e)
    finally:
        cursor.close()
        return is_success


# internal function for debug, will return all users from db
def print_all():
    try:
        sql = "SELECT * FROM QzeMAiiWP6.users;"
        cursor = querydb(sql)
        for row in cursor:
            print(row)
    finally:
        cursor.close()


# function will return TRUE if user exist in the table
def is_id_exist(user_id):
    isexist = False
    try:
        sql = "SELECT * FROM QzeMAiiWP6.users where user_id = %s;" % user_id
        cursor = querydb(sql)
        if cursor.rowcount > 0:
            isexist = True
    except Exception as e:
        print("general error when trying to get user from DB ", e)
    finally:
        cursor.close()
        return isexist


# function will return name for specific id
def get_user_name_by_id(user_id):
    result_name = ''
    try:
        sql = "SELECT user_name FROM QzeMAiiWP6.users where user_id = %s;" % user_id
        cursor = querydb(sql)
        result = cursor.fetchone()
        result_name = result['user_name']
    except Exception as e:
        print("general error when trying to get user name from DB ", e)
    finally:
        cursor.close()
        return result_name
