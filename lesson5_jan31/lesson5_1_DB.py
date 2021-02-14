# pip install pymysql
import pymysql
# DB connection:
# Username: QzeMAiiWP6
# Database name: QzeMAiiWP6
# Password: r8Dopb5X8y
# Server: remotemysql.com
# Port: 3306
# example code https://github.com/Dgotlieb/Python-MySQL

user = 'QzeMAiiWP6'
password = 'r8Dopb5X8y'
dbname = 'QzeMAiiWP6'
schema = 'QzeMAiiWP6'
host = 'remotemysql.com'

def selectall():
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='QzeMAiiWP6', passwd='r8Dopb5X8y', db='QzeMAiiWP6')

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Getting all data from table “users”
    cursor.execute("SELECT * FROM QzeMAiiWP6.users;")

    # Iterating table and printing all users
    for row in cursor:
        print(row)

    cursor.close()
    conn.close()


def insert(name, id):
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=dbname)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute("INSERT into QzeMAiiWP6.users (name, id) VALUES ('%s', %d)" % (name, id))

    cursor.close()
    conn.close()


def delete(name):
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=dbname)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Deleting data into table
    cursor.execute("DELETE FROM %s.users WHERE name = '%s'" % (schema, name))

    cursor.close()
    conn.close()


def updateid(name):
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=3306, user=user, passwd=password, db=dbname)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Deleting data into table
    cursor.execute("UPDATE %s.users SET id = '10' WHERE name = 'u2'" % schema)

    cursor.close()
    conn.close()


# insert('u2',2)
# delete("john")
selectall()
# updateid("aaa")
selectall()