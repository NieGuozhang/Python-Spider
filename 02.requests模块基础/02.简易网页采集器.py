"""
需求：简易网页采集器，爬取搜狗指定词条对应的搜索结果页面

UA：User-Agent，请求载体的身份标识
UA检测：门户网站的服务会检测对应请求载体的身份标识，如果检测到请求的载体身份标识是一款浏览器，
说明该请求是一个正常的请求。但是如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示该请求是不正常的请求。
则服务器端很有可能拒绝该次请求。

UA伪装：让爬虫对应的请求载体伪装成一款浏览器
"""

import requests


def main():
    # 1.指定URL
    url = 'https://www.sogou.com/web'
    # 处理URL的携带参数：封装到字典中
    kw = input('enter a word:')
    params = {
        'query': kw,
    }

    # UA伪装 将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    # 2.对指定的URL发起请求是携带参数的，并且请求过程中已经处理参数
    response = requests.get(url=url, params=params, headers=headers)

    # 3.获取响应数据
    paga_text = response.text

    # 4.数据持久化
    filename = kw + '.html'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(paga_text)
    print(filename, '保存成功！')


    
if __name__ == '__main__':
    main()
