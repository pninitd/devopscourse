from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# The frontend test will:
# 1. Start a Selenium Webdriver session.
# 2. Navigate to web interface URL using an existing user id.
# 3. Check that the user name element is showing (web element exists).
# 4. Print user name (using locator).


def frontend_test(user_id, expected_name):
    status = False
    driver = webdriver.Chrome(executable_path="/Users/pninitds/PycharmProjects/chromedriver")
    # open selenium an go the the web app url
    url = 'http://127.0.0.1:5001/users/get_user_data/%d' % user_id
    driver.get(url)

    try:
        # check user name element exists
        user_name = driver.find_element_by_id('user').text
        print('frontend_test: user_name is', user_name, ', for id:', user_id)
        assert len(user_name) > 0
        assert user_name == expected_name
        status = True
    except NoSuchElementException as e:
        print("No Such Element", e)
    except WebDriverException as e:
        print("Error", e)
    except Exception as e:
        print("failed test")
    finally:
        driver.quit()
        return status


def main():
    user_id = 1
    user_name = 'pninit'
    success = frontend_test(user_id, user_name)
    if success:
        print('Test finished successfully')
    else:
        raise Exception("test failed")


if __name__ == '__main__':
    main()
