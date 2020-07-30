import requests
from lxml import etree
import chaojiying


def main():
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }
    page_text = requests.get(url=url, headers=headers).text

    # 解析验证码图片img中src属性值
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.HTML(page_text, parser=parser)
    code_img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = requests.get(url=code_img_src, headers=headers).content
    # 将验证码保存至本地
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)

    # 调用打码平台的示例代码进行验证码图片识别
    code = chaojiying.getCodeText('code.jpg', 1902)
    print(code)


if __name__ == '__main__':
    main()

    
