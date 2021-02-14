import json

import pymysql

db_con = ''
db_cur = ''


def open_connection():
    user = 'QzeMAiiWP6'
    password = 'r8Dopb5X8y'
    dbname = 'QzeMAiiWP6'
    schema = 'QzeMAiiWP6'
    host = 'remotemysql.com'
    port = 3306

    global db_con
    # Establishing a connection to DB
    db_con = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbname, cursorclass=pymysql.cursors.DictCursor)
    db_con.autocommit(True)


def querydb(sql):
    if db_con == '':
        # open connection
        open_connection()

    # Getting a cursor from Database
    global db_cur
    db_cur = db_con.cursor()

    # Getting all data from table “users”
    db_cur.execute(sql)


def insert_dogs(name, age, breed):
    sql = "INSERT into QzeMAiiWP6.dogs (name, age, breed) VALUES ('%s', %d, '%s');" % (name, age, breed)
    querydb(sql)
    return True


def update_dog_age(name, age):
    sql = "UPDATE QzeMAiiWP6.dogs SET age = %d WHERE name ='%s';" % (age, name)
    querydb(sql)


def delete_dog_by_name(name):
    sql = "DELETE FROM QzeMAiiWP6.dogs WHERE name ='%s';" % name
    querydb(sql)


def print_dogs_name():
    sql = "SELECT name FROM QzeMAiiWP6.dogs;"
    querydb(sql)
    for row in db_cur:
        print(row)


# function for part 2
def print_all_as_json():
    sql = "SELECT * FROM QzeMAiiWP6.dogs;"
    querydb(sql)
    data = db_cur.fetchall()
    results = json.dumps(data, indent=2)
    # print(results)
    return results

# print_all_as_json()


def close_connection():
    if db_cur != '':
        db_cur.close()
    if db_con != '':
        db_con.close()

# 1
# DataGrip ddl:
# create table dogs
# (
# 	name varchar(40) not null,
# 	age int not null,
# 	breed varchar(30) not null
# );


# 2
# insert_dogs('peki', 2, 'pekingese')
# insert_dogs('goldi', 3, 'golden retriever')
# insert_dogs('arthur', 4, 'shih tzu')

# 3
# update_dog_age('goldi', 1)

# 4
# delete_dog_by_name('arthur')

# 5
# print_dogs_name()


# close all connections
close_connection()
