from selenium import webdriver
from lxml import etree
import time

# 实例化一个浏览器对象(传入浏览器驱动)
browser = webdriver.Chrome(executable_path='./chromedriver')

# 让浏览器发起一个指定URL请求
browser.get('http://125.35.6.84:81/xk/')

# 获取浏览器当前页面的页面源码数据
page_text = browser.page_source

# 解析数据
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.HTML(page_text, parser=parser)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

time.sleep(5)
browser.quit()
