"""
需求：爬取豆瓣电影分类排行榜

"""
import requests
import json


def main():
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '1',  # 从库中的第几部电影去取
        'limit': '20',  # 一次取出的个数
    }

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    # 发起get请求
    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()

    # 数据持久化
    with open('./douban.json', 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp=fp, ensure_ascii=False)

    print('爬取完毕！')


    
if __name__ == '__main__':
    main()
