# Extra3: Create another table to write your users data and save the date as DATETIME (and not varchar).
# I fix only insert, get, isexist functions to accommodate with this new table, didn't have time to make it more generic.
from datetime import datetime, time

from project_first_part.db_connector import open_connection, querydb


# create another users table with datetime
def create_tbl():
    connection = open_connection()
    sql_tbl = "create table IF NOT EXISTS users2 (user_id int not null primary key,user_name varchar(50) not null,creation_date datetime null)"
    try:
        cursor = connection.cursor()
        cursor.execute(sql_tbl)
    finally:
        # Close connection.
        connection.close()


# function will create a new user and return TRUE if success
def create_user(user_id, name):
    is_success = False
    try:
        now = datetime.now()
        sql = "INSERT into QzeMAiiWP6.users2 (user_id, user_name, creation_date) VALUES (%s, '%s', '%s');" % (user_id, name, now)
        cursor = querydb(sql)
        if cursor.rowcount > 0:
            is_success = True
    except Exception as e:
        print("general error when trying to create new user in DB ", e)
    finally:
        cursor.close()
        return is_success


# internal function for debug, will return all users from db
def print_all_users():
    try:
        sql = "SELECT * FROM QzeMAiiWP6.users2;"
        cursor = querydb(sql)
        for row in cursor:
            print(row)
    finally:
        cursor.close()


# function will return TRUE if user exist in the table
def is_id_exist(user_id):
    isexist = False
    try:
        sql = "SELECT * FROM QzeMAiiWP6.users2 where user_id = %s;" % user_id
        cursor = querydb(sql)
        if cursor.rowcount > 0:
            isexist = True
    except Exception as e:
        print("general error when trying to get user from DB ", e)
    finally:
        cursor.close()
        return isexist


def main():
    id = 1
    name = 'p'

    # test the new table
    create_tbl()
    # check if id already exist in db
    if not is_id_exist(id):
        # create a new user in the new table
        is_success = create_user(id, name)
        if is_success:
            print_all_users()
    else:
        print("user already exist")


if __name__ == '__main__':
    main()
