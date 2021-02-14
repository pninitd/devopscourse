from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/pninitds/PycharmProjects/chromedriver")
driver.get("https://filebin.net/")
driver.find_element_by_id("fileField").send_keys('/Users/pninitds/tmp.txt')

driver.quit()


#headless
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(executable_path="/Users/pninitds/PycharmProjects/chromedriver", options=options)