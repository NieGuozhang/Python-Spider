from selenium import webdriver
from time import sleep
# 实施无可视化界面
from selenium.webdriver.chrome.options import Options
# 规避检测
from selenium.webdriver import ChromeOptions

# 无可视化界面设置
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 如何让selenium规避被检测到的风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options, options=option)

# 无可视化界面（无头浏览器）
browser.get('http://www.baidu.com')

print(browser.page_source)
sleep(2)
browser.quit()
