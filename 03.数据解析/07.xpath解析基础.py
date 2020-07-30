from lxml import etree


def main():
    # 若出现html代码书写不规范，不符合xml解析器的使用规范，使用parse方法的parser参数
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('sougou.html', parser=parser)
    r = tree.xpath('//div[@class="top-nav"]//@href')
    print(r)


if __name__ == '__main__':
    main()

    
