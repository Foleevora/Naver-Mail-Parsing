__author__ = "Foleevora"
__version__ = "1.0.0"
__email__ = "foleevora@gmail.com"

import sys
import time
from selenium import webdriver

def parsing(id, pwd):
    driver = webdriver.Chrome('/Users/user_name/Downloads/chromedriver')
    driver.set_window_size(1120, 550)

    driver.get("https://nid.naver.com/nidlogin.login")

    elem_id = driver.find_element_by_id("id")
    elem_id.send_keys(id)
    elem_pwd = driver.find_element_by_id("pw")
    elem_pwd.send_keys(pwd)
    form = driver.find_element_by_id("frmNIDLogin")
    form.submit()

    time.sleep(1)

    driver.get("http://mail.naver.com")
    elem_li = driver.find_elements_by_class_name("unmark")

    for li in elem_li:
        sender = li.find_element_by_class_name("name").find_element_by_tag_name("a").text
        title = li.find_element_by_class_name("subject").find_element_by_class_name("mail_title").text
        print(sender + " - " + title)

    driver.quit()


if __name__ == "__main__":

    if len(sys.argv) is not 3:
        print("UASGE: NaverMailParsing.py [ID] [PWD]")
    else:
        parsing(sys.argv[1], sys.argv[2])
