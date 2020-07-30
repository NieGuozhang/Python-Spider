"""
需求：爬取三国演义小说所有的章节标题和章节内容 http://www.shicimingju.com/book/sanguoyanyi.html
"""

import requests
from bs4 import BeautifulSoup
import os


def main():
    if not os.path.exists('./三国演义'):
        os.mkdir('./三国演义')

    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }
    page_text = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(page_text, 'lxml')
    # 得到页面中的所有标题a标签
    a_list = soup.select('.book-mulu > ul a')

    # 循环获取每章的url和标题，并写入文件
    for item in a_list:
        # 获取每章的URL
        text_url = 'http://www.shicimingju.com' + item['href']
        # print(text_url)
        # 获取每章的页面源代码
        article_page = requests.get(url=text_url, headers=headers).text
        # print(article_page)
        soup = BeautifulSoup(article_page, 'lxml')
        # print(soup.find('div', class_='.chapter_content'))
        # 获取每章的文本内容
        text = soup.find('div', class_='chapter_content').text
        filename = item.text + '.txt'
        filepath = './三国演义/' + filename
        # 写文件
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(text)
        print(filename, '爬取完毕！')
    print('全部爬取完毕！')


    
if __name__ == '__main__':
    main()
