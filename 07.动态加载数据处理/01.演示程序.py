from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 打开Chrome浏览器
# 'r'是防止字符转义的
driver = webdriver.Chrome(r'./chromedriver')
# 浏览器最大化
driver.maximize_window()
# 打开猿人学首页
driver.get('https://www.yuanrenxue.com')
time.sleep(3)

# 滑动到页面中间处
driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2)")
time.sleep(3)

# 滑动到页面最下方
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

# 滑动到页面最上方
driver.execute_script("window.scrollTo(0,0)")
time.sleep(3)

# 通过html的class属性来定位链接位置，并点击
driver.find_element_by_class_name('slide-left').click()
time.sleep(3)

# 定位页面右上角的搜索图标并点击
driver.find_element_by_class_name('search-show').click()

# 找到输入框
search = driver.find_element_by_class_name("search-input")
# 输入 Python教程
search.send_keys(u'python教程')
time.sleep(7)
# 回车
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
