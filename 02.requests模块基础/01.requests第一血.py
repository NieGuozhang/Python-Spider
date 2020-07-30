"""
需求：爬取搜狗首页的页面数据
"""
import requests


def main():
    # step1:指定URL
    url = 'https://www.sogou.com/'

    # step2：发起请求
    # get方法会返回一个响应对象
    response = requests.get(url=url)

    # step3:获取响应数据，
    # text返回的是页面对应的源码数据，字符串形式
    page_text = response.text
    print(page_text)

    # step4:数据持久化
    with open('../03.数据解析/sougou.html', 'w', encoding='utf-8') as file:
        file.write(page_text)
    print('爬取数据结束')


    
if __name__ == '__main__':
    main()
