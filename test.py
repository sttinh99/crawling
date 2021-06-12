from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# khai bao bien

browser = webdriver.Chrome(executable_path="chromedriver.exe")

# test open web

browser.get("https://facebook.com")

# Dien thong tin vao email va fb

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("sttinh1103")

txtPassword = browser.find_element_by_id("pass")
txtPassword.send_keys("passfacebook")

# submit form

txtPassword.send_keys(Keys.ENTER)

# Stop program 5s

sleep(5)


# Dong trinh duyen

browser.close()
