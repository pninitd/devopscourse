# Class 4 Assignment and Challenges
# By: Maher Kabour (maher.kabour@peer39.com)

# Exercises arranged in functions. Each function returns its webdriver(s),
# so that Python does not auto-kill the drivers once the function is done.
# Cleanup of drivers is done at end of script, controlled with quit_drivers variable.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# change driver location to match your system
chrome_driver_exe = r"driver\chromedriver.exe"
gecko_driver_exe = r"driver\geckodriver.exe"  # only used in first exercise
quit_drivers = False
maximize_windows = True


def ex1():
    try:
        chromedriver = webdriver.Chrome(executable_path=chrome_driver_exe)
        if maximize_windows:
           chromedriver.maximize_window()
        chromedriver.get("http://www.walla.co.il")
    except Exception as e:
        print("Error with opening Chrome driver", e)

    try:
        firefoxdriver = webdriver.Firefox(executable_path=gecko_driver_exe)
        if maximize_windows:
            firefoxdriver.maximize_window()
        firefoxdriver.get("http://www.ynet.co.il")
    except Exception as e:
        print("Error with opening Gecko driver", e)

    return [chromedriver, firefoxdriver]


def ex2():
    chromedriver = webdriver.Chrome(executable_path=chrome_driver_exe)
    if maximize_windows:
        chromedriver.maximize_window()
    chromedriver.get("https://google.com")
    title1 = chromedriver.title
    chromedriver.refresh()
    if chromedriver.title == title1:
        print("we have the same title")
    return [chromedriver]


def ex3():
    # 3 - open multiple drivers, locate same element and compare results
    # for this exercise we'll open 5 chrome drivers on "https://www.google.com",
    # and we'll locate the search text box, expecting it to be on a specific xpath

    # expected xpath of the text box, taken manually from page inspection
    google_search_box = r'/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input'

    # open 5 drivers
    drivers = []
    for i in range(5):
        drivers.append(webdriver.Chrome(executable_path=chrome_driver_exe))

    for d in drivers:
        try:
            if maximize_windows:
                d.maximize_window()
            d.get("https://www.google.com")
            element = d.find_element_by_xpath(google_search_box)
            print(element.location)
        except Exception as e:
            print("Couldn't find textbox at expected xpath, or something went wrong", e)

    return drivers


def ex4():
    # 4 - Send some Hebrew text for translation on google translate
    translate_driver = webdriver.Chrome(executable_path=chrome_driver_exe)
    if maximize_windows:
        translate_driver.maximize_window()
    translate_driver.get("https://translate.google.com")
    gtranslate_text_box = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea"
    element = translate_driver.find_element_by_xpath(gtranslate_text_box)
    if element.is_enabled():
        element.send_keys("קצת טקסט בעברית לבדיקת תרגום")
        element.send_keys(Keys.ENTER)
    return [translate_driver]


def ex5():
    # 5 - Search for a song on youtube, activate with button
    youtube_driver = webdriver.Chrome(executable_path=chrome_driver_exe)
    if maximize_windows:
        youtube_driver.maximize_window()
    youtube_search_box = '//*[@id="search"]'
    youtube_search_button = '//*[@id="search-icon-legacy"]'
    my_song = "Novermber Rain"

    youtube_driver.get("https://www.youtube.com")
    try:
        youtube_driver.find_element_by_xpath(youtube_search_box).send_keys(my_song)
        youtube_driver.find_element_by_xpath(youtube_search_button).click()
    except Exception as e:
        print("Something went wrong", e)
    finally:
        return [youtube_driver]


def ex6():
    # 6 - Locate google translate input text box by 3 locators
    translate_driver = webdriver.Chrome(executable_path=chrome_driver_exe)
    if maximize_windows:
        translate_driver.maximize_window()
    translate_driver.get("https://translate.google.com")
    textbox_xpath = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea"
    textbox_class = "er8xn"
    textbox_attribute = '//textarea[@aria-label="Source text"]'

    # find by class:
    element = translate_driver.find_element_by_class_name(textbox_class)
    element.send_keys("Found you by Class!")
    element.send_keys(Keys.ENTER)
    print(element)

    # find by attribute (attribute: aria-label)
    element = translate_driver.find_element_by_xpath(textbox_attribute)
    element.send_keys("Found you by Attribute!")
    element.send_keys(Keys.ENTER)
    print(element)

    # find by absolute xpath
    element = translate_driver.find_element_by_xpath(textbox_xpath)
    element.send_keys("Now I got you Absolutely!")
    print(element)

    return [translate_driver]


def ex7():
    # 7 - Facebook login
    my_email = "myemail@bestemail.net"
    my_password = "guess!"
    login_email_xpath = '//*[@id="email"]'
    login_password_xpath = '//*[@id="pass"]'
    login_button_xpath = '//*[@id="u_0_b"]'

    facebook_driver = webdriver.Chrome(chrome_driver_exe)
    if maximize_windows:
        facebook_driver.maximize_window()
    facebook_driver.get('https://www.facebook.com')
    facebook_driver.find_element_by_xpath(login_email_xpath).send_keys(my_email)
    facebook_driver.find_element_by_xpath(login_password_xpath).send_keys(my_password)
    facebook_driver.find_element_by_xpath(login_button_xpath).click()

    return [facebook_driver]


def ex8():
    # Challenge 1 - delete all cookies and print them to verify
    # We open a couple of websites to get some cookies, we print them, delete, and print again to verify no cookies left
    cookie_driver = webdriver.Chrome(chrome_driver_exe)
    if maximize_windows:
        cookie_driver.maximize_window()
    cookie_driver.get("https://google.com")
    cookie_driver.get("https://yahoo.com")
    for cookie in cookie_driver.get_cookies():
        print("Found a cookie:")
        print("    " + str(cookie))
    print("### DELETING COOKIES ###")
    cookie_driver.delete_all_cookies()
    print("Printing all cookies (expecting none):")
    print(str(cookie_driver.get_cookies()))
    return [cookie_driver]


def ex9():
    # Challenge 2 - Search github for selenium
    github_searchbox_name = 'q'
    github_driver = webdriver.Chrome(chrome_driver_exe)
    # Github search will fail if window is too small and not showing search bar
    github_driver.maximize_window()
    github_driver.get("https://github.com")
    github_driver.find_element_by_name(github_searchbox_name).send_keys("selenium" + Keys.ENTER)
    return [github_driver]


list_of_drivers = []

# Uncomment an exercise to run
# list_of_drivers.extend(ex1())
# list_of_drivers.extend(ex2())
# list_of_drivers.extend(ex3())
# list_of_drivers.extend(ex4())
# list_of_drivers.extend(ex5())
# list_of_drivers.extend(ex6())
# list_of_drivers.extend(ex7())
# list_of_drivers.extend(ex8())
# list_of_drivers.extend(ex9())

# cleanup
if quit_drivers and list_of_drivers:
    for d in list_of_drivers:
        d.close()