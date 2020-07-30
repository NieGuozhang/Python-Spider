"""
需求：爬取糗事百科中糗图板块下所有的糗图图片
"""
import requests
import re

import os


def main():
    # 创建一个文件夹，用来保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    # UA伪装 将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    for i in range(1, 14):
        url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(i)

        # 使用通用爬虫对URL对应的一整张页面进行爬取
        page_text = requests.get(url=url, headers=headers).text  # 得到源码数据

        # 使用聚焦爬虫，将页面中所有的糗图进行提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)
        # print(img_src_list)
        for src in img_src_list:
            # 拼接出一个完整的图片地址
            src = 'https:' + src
            # 请求到了图片数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片
            img_name = src.split('/')[-1]
            # 图片最终存储的路径
            img_path = './qiutuLibs/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功！')
        print('第{}页爬取完毕！'.format(i))
    print('所有页面爬取完成！')


    
if __name__ == '__main__':
    main()
