#test selenium driver
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/pninitds/PycharmProjects/chromedriver")
driver.get("https://translate.google.com")
print(driver.current_url)
print(driver.title)
# print(driver.page_source)

# navigate browser history
# driver.forward()
# driver.back()
# driver.refresh()

# my_list = driver.find_element_by_link_text("History")
testarea = driver.find_element_by_xpath('//textarea')
elements = driver.find_elements_by_class_name("er8xn")
testarea.send_keys("abc")
testarea.send_keys(Keys.ENTER)
print(len(elements))

# get any attribute from the element
print(testarea.get_attribute("autocomplete"))

#sleep
# time.sleep(3)

# for each findelement or findelemnts wait up to 10 sec per search.
driver.implicitly_wait(10)
# explicitly wait - wait for specific element

#inject javascript
#driver.execute("")

# close current window
driver.close()
# close all
driver.quit()

