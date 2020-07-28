"""
编码流程
1、验证码的识别，获取验证码图片的文字数据
2、对POST请求进行发送（处理请求参数）
3、对响应数据持久化存储
"""

import requests
import chaojiying
from lxml import etree


def main():
    session = requests.Session()
    url = 'http://www.renren.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'
    }
    page_text = session.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
    code_img_data = session.get(url=code_img_src, headers=headers).content
    # 保存验证码图片
    with open('./code.jpg', 'wb') as fp:
        fp.write(code_img_data)

    # 使用超级鹰代码对验证码图片进行识别
    code_str = chaojiying.getCodeText('code.jpg', 1902)
    print('验证码：', code_str)

    # login_url = tree.xpath('//*[@id="loginForm"]/@action')
    login_url = 'http://www.renren.com/PLogin.do'

    data = {
        'email': 'XXX',
        'password': 'XXX',
        'icode': code_str,
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'f': '',
    }
    # 通用验证登录成的方式是看响应状态码
    response = session.post(url=login_url, headers=headers, data=data)
    print(response.status_code)
    resp = session.get(url='http://www.renren.com/974823124/profile', headers=headers).text
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(resp)
    print('爬取完毕！')


if __name__ == '__main__':
    main()
