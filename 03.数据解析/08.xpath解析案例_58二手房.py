"""
需求：爬取58二手房中的房源信息
"""
import requests
from lxml import etree


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    url = 'https://wh.58.com/ershoufang/'
    # 获取HTML页面源码数据
    page_text = requests.get(url=url, headers=headers).text
    parser = etree.HTMLParser(encoding="utf-8")

    # 解析数据
    tree = etree.HTML(page_text, parser=parser)
    # 存储的就是li标签对象
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt', 'w', encoding='utf-8')
    for li in li_list:
        # 局部解析，前面需要加'.'
        title = li.xpath('./div[2]/h2/a/text()')[0]
        fp.write(title + '\n')
    fp.close()
    print('爬取完毕！')


if __name__ == '__main__':
    main()

    
