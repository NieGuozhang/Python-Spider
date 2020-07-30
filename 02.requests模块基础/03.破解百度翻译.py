"""
需求：破解百度翻译

post请求，携带参数
响应数据是一组json数据
"""

import requests
import json


def main():
    # 1.指定URL
    post_url = 'https://fanyi.baidu.com/sug'
    # 处理post请求中URL的携带参数：封装到字典中
    kw = input('enter a word:')
    data = {
        'kw': kw,
    }

    # UA伪装 将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    # 2.发起POST请求
    response = requests.post(url=post_url, data=data, headers=headers)

    # 3.获取响应数据,返回的是一个obj对象(如果确认响应数据是json类型的，才可以使用json())
    dict_obj = response.json()
    # print(dict_obj)

    # 4.数据持久化
    filename = kw + '.json'
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dict_obj, fp=file, ensure_ascii=False)
    print(filename, '保存成功！')


    
if __name__ == '__main__':
    main()
