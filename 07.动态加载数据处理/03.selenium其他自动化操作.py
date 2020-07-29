from selenium import webdriver
import time

browser = webdriver.Chrome(r'./chromedriver')

browser.get('https://www.taobao.com')

# 标签定位
search_input = browser.find_element_by_id('q')

# 标签交互
search_input.send_keys('Iphone')

# 执行一组js程序, 让屏幕拖动一屏幕的高度
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)

# 点击搜索按钮
button = browser.find_element_by_class_name('btn-search')
button.click()  # 按钮点击

browser.get('http://www.baidu.com')
time.sleep(2)

# 回退
browser.back()

# 前进
browser.forward()


time.sleep(5)
browser.quit()
