"""
需求：
"""
import requests
from lxml import etree
import os


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }
    url = 'http://pic.netbian.com/4kmeinv/'
    response = requests.get(url=url, headers=headers)
    # 可以手动设定响应数据的编码格式
    # response.encoding = 'utf-8'

    page_text = response.text
    parser = etree.HTMLParser(encoding="utf-8")
    # 解析页面:src属性值，alt属性值
    tree = etree.HTML(page_text, parser=parser)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    # 创建一个文件夹
    if not os.path.exists('./pictures'):
        os.mkdir('./pictures')

    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 通用处理中文乱码的解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_src, img_name)

        # 请求图片进行持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'pictures/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        print(img_name, '下载成功！')
    print('所有图片下载完成！')


if __name__ == '__main__':
 
    main()
