"""
需求：爬取国家药品监督管理局中基于中华人民共和国化妆品生产许可证相关数据

动态加载数据
首页中对应的企业信息数据是通过Ajax动态请求得到的。

http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=ff83aff95c5541cdab5ca6e847514f88
通过对详情页的URL分析：
- URL的域名都是一样的，只是携带的参数id是不一样的
- id可以从首页对应的ajax请求到的json串中获取
- 域名和id进行拼接就可以得到一个企业详情页的URL
- 详情页的企业详情数据也是动态加载出来的


"""
import requests
import json


def main():
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    id_list = []  # 存储企业ID
    # 参数封装
    for page in range(1, 20):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,  # 获取第几页
            'pageSize': '15',  # 每页获取多少
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    # print(id_list)

    # 获取企业详情数据
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    all_data_list = []
    for id in id_list:
        data = {
            'id': id,
        }
        detail_json = requests.post(url=post_url, data=data, headers=headers).json()
        # print(detail_json, '---------ending------------')
        all_data_list.append(detail_json)

    # 持久化存储all_data_list
    with open('./all_data_list.json', 'w', encoding='utf-8') as fp:
        json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('爬取完毕！')

    

if __name__ == '__main__':
    main()
