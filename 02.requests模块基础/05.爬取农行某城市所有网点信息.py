"""
需求：输入城市名，获取这个城市的所有农业银行网点位置等信息
"""

import requests
import json


def main():
    url = 'http://app.abchina.com/branch/common/BranchService.svc/Branch'
    city = input('请输入要爬取的城市名称：')

    params = {
        'p': '-1',
        'c': '-1',
        'b': '-1',
        'q': city,
        't': '1',
        'z': '0',
        'i': '0', # 爬取第多少页的数据
    }

    # UA伪装 将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()

    # 持久化数据
    filename = city + '.json'
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp=fp, ensure_ascii=False)

    print('爬取完毕！')


if __name__ == '__main__':
    main()
