"""
需求：爬取所有城市名称
"""

import requests
from lxml import etree
import os


def main():
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    # }
    #
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url, headers=headers).text
    #
    # parser = etree.HTMLParser(encoding="utf-8")
    # tree = etree.HTML(page_text, parser=parser)
    # hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # # 解析到了热门城市的名字
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    #
    # all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in all_li_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    # print(all_city_names)
    # print(len(all_city_names))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text

    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.HTML(page_text, parser=parser)
    # 解析到热门城市和所有城市对应的标签a
    # //div[@class="bottom"]/ul/li/a 热门城市的a标签层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a 所有城市的a标签的层级关系
    # a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    a_list = tree.xpath('//div[@class="bottom"]/ul//li/a ')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names)
    print(len(all_city_names))


if __name__ == '__main__':
    main()

    
