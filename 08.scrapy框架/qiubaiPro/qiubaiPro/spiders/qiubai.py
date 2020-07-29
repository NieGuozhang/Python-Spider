import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 解析作者的名称+段子内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            # xpath返回的是列表，列表元素是selector类型的对象
            # extract()可以将selector对象中对应的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            # 列表调用extract()方法则表示将列表中每一个selector对象中的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)  # 转化为字符串
            print(author, content)
            break
