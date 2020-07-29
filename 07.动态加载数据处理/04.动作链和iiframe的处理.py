from selenium import webdriver
from selenium.webdriver import ActionChains  # 导入动作链
import time

browser = webdriver.Chrome('./chromedriver')

browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位标签是存在于iframe标签中，则必须通过如下操作进行标签定位
browser.switch_to.frame('iframeResult')  # 切换浏览器标签的作用域
div = browser.find_element_by_id('draggable')
# print(div)

"""
动作链
"""
# 实例化一个action
action = ActionChains(browser)
# 点击长按指定的额标签
action.click_and_hold(div)

for i in range(5):
    # perform()表示动作立即执行动作链操作
    # move_by_offset(x, y) x表示水平方向的偏移，y表示竖直方向的偏移
    action.move_by_offset(17, 0).perform()
    time.sleep(3)

# 释放动作链
action.release()

browser.quit()
