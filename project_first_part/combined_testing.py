from project_first_part.backend_testing import check_new_user_creation, check_user_in_db, check_get_user

# The combined test will:
# Post any new user data to the REST API using POST method.
# Submit a GET request to make sure data equals to the posted data.
# Using pymysql, check posted data was stored inside DB (users table).
# Start a Selenium Webdriver session.
# Navigate to web interface URL using the new user id.
# Check that the user name is correct.

# Any failure will throw an exception using the following code: raise Exception("test failed")


from project_first_part.frontend_testing import frontend_test

# Test params: receive a user
user_id = int(input("insert user id: "))
user_name = (input("insert user name: "))

# 1. Post new user data
iscreated = check_new_user_creation(user_id, user_name)
if iscreated is False:
    raise Exception("test failed")

# 2. GET request to make sure data equals to the posted data
isequal = check_get_user(user_id, user_name)
if isequal is False:
    raise Exception("test failed")

# 3. posted data was stored inside DB
user_name_from_db = check_user_in_db(user_id, user_name)
print('user name from DB is:', user_name_from_db )
if user_name_from_db == '':
    raise Exception("test failed")

# 4. Check that the user name is correct using Selenium
issuccess = frontend_test(user_id, user_name)
if issuccess:
    print('Test finished successfully')
else:
    raise Exception("test failed")
