"""
需求：爬取糗事百科中糗图板块下所有的糗图图片
"""

import requests


def main():
    # 如何爬取图片数据
    url = 'https://www.qiushibaike.com/article/123407983'
    # content返回的是2进制形式的图片数据
    # text(字符串) content（二进制） json（对象）
    img_data = requests.get(url=url).content

    # 持久化数据
    with open('./qiutu.jpg', 'wb') as fp:
        fp.write(img_data)


if __name__ == '__main__':
    main()
