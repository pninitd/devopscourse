from selenium import webdriver

# 1a
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/pninitds/PycharmProjects/chromedriver")
driver.get("http://www.walla.co.il")

# 1b
driver = webdriver.Firefox(executable_path="/Users/pninitds/PycharmProjects/geckodriver")
driver.get("http://www.ynet.co.il")

# 2
title = driver.title
driver.refresh()
if title == driver.title:
    print("Equal")
else:
    print("Title is not equal")

# returning back to use chrome..
driver.close()
driver = webdriver.Chrome(executable_path="/Users/pninitds/PycharmProjects/chromedriver")


# 3
# yes - element will have same locators in all browsers

# 4
driver.get("http://translate.google.com")
driver.find_element_by_xpath('//textarea').send_keys("גנן גידל דגן בגן")

# 5
driver.get("https://www.youtube.com")
driver.find_element_by_id("search").send_keys("above and beyond")
driver.find_element_by_id("search-icon-legacy").click()

# 6
driver.get("http://translate.google.com")
locator1 = driver.find_element_by_class_name("er8xn")
locator2 = driver.find_element_by_xpath("//textarea[@aria-label='Source text']")
locator3 = driver.find_element_by_css_selector("textarea.er8xn")
print(locator1)
print(locator2)
print(locator3)

# 7
driver.get("https://facebook.com")
driver.find_element_by_id("email").send_keys("blabla@gmail.com")
driver.find_element_by_id("pass").send_keys("12345678")
driver.find_element_by_name("login").click()

# 8
driver.get("https://ynet.co.il")
print("before deleting cookies: ", driver.get_cookies())
driver.delete_all_cookies()
print("after deleting cookies: ", driver.get_cookies())

# 9
driver.get("https://github.com/")
try:
    driver.find_element_by_class_name("form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus ").send_keys("Selenium").send_keys(Keys.ENTER)
except NoSuchElementException as e:
    print("You are not logged in to github")
finally:
    driver.quit()
