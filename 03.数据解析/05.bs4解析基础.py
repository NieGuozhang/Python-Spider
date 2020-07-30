from bs4 import BeautifulSoup


def main():
    # 将本地的html文档加载到该对象中
    # 参数2固定
    fp = open('./sougou.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup.a) # soup.tagName返回的是HTML中第一次出现的tagName标签
    # print(soup.find('a')['href'])  # 作用和soup.a一样
    # 返回class为top-nav的div
    print(soup.find('div', class_='top-nav').text)
    # print(soup.findAll('a'))
    # print(soup.select('.top-nav'))

    # print(soup.select('.top-nav > ul a').get_text())


if __name__ == '__main__':
    main()

    
