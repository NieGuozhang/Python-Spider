from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

browser = webdriver.Chrome('./chromedriver')

browser.get('https://qzone.qq.com')

browser.switch_to.frame('login_frame')
a_tag = browser.find_element_by_id('switcher_plogin')
a_tag.click()

input_username = browser.find_element_by_id('u')
input_password = browser.find_element_by_id('p')

sleep(1)
input_username.send_keys('QQ号')
sleep(1)
input_password.send_keys('QQ密码')
sleep(1)

login_button = browser.find_element_by_id('login_button')
login_button.click()

browser.quit()
