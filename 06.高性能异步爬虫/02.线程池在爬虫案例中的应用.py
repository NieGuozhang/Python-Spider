"""
需求：爬取梨视频的视频数据

线程池使用的原则：线程池处理的是阻塞且较为耗时的操作
"""
import requests
from lxml import etree
import re
import os
from multiprocessing.dummy import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
}


def main():
    # 对下述URL发起请求解析出视频详情页的URL和视频的名称
    url = 'https://www.pearvideo.com/category_5'
    page_text = requests.get(url=url, headers=headers).text
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.HTML(page_text, parser=parser)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')

    video_list = []  # 保存所有视频的URL地址和名字
    for li in li_list:
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'

        # 对详情页发起请求
        detail_page_text = requests.get(url=detail_url, headers=headers).text

        # 从详情页中解析出视频的地址url
        # 由于url在js文件中，不能采用bs4和xpath，只能用正则匹配的方式
        ex = 'srcUrl="(.*?)",vdoUrl'
        video_url = re.findall(ex, detail_page_text)[0]

        dict = {
            'name': name,
            'url': video_url,
        }
        video_list.append(dict)

    # 创建文件夹用于保存视频
    if not os.path.exists('./梨视频'):
        os.mkdir('./梨视频')

    # 使用线程池来处理耗时的请求操作
    pool = Pool(4)
    pool.map(get_video_data, video_list)
    pool.close()
    pool.join()


def get_video_data(dic):
    video_url = dic['url']
    print(dic['name'], '正在下载。。。。。。')
    data = requests.get(url=video_url, headers=headers).content
    video_path = '梨视频/' + dic['name']
    with open(video_path, 'wb') as fp:
        fp.write(data)
        print(dic['name'], '下载成功！')


if __name__ == '__main__':
    main()
