import requests
import re
import os


def main():
    if not os.path.exists('文件夹'):
        os.mkdir('文件夹')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }

    for page in range(1, 8):
        page = str(page)
        url = '指定URL地址{}'.format(page)
        page_text = requests.get(url=url, headers=headers).text

        ex = '<div class="p-img">.*?<img width=".*?src="(.*?)" data-lazy-img=".*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)

        for src in img_src_list:
            src = 'https:' + src
            img_name = src.split('/')[-1]
            img_path = './' + img_name
            img_data = requests.get(url=src, headers=headers).content
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
        print('第{}页爬取完毕！'.format(page))
    print('爬取完毕！')


if __name__ == '__main__':
    main()
