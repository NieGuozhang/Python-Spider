import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称：就是爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名列表：用来限定start_urls列表中哪些可以被请求
    # allowed_domains = ['http://www.baidu.com']

    # 起始的URL列表:该列表中存放的URL会被scrapy自动进行请求发送
    start_urls = ['http://www.baidu.com/', 'Https://www.sogou.com']

    # 用作于数据解析：response参数表示的就是请求成功后对应的响应对象
    # parse会被调用多次，次数是start_urls的列表长度
    def parse(self, response):
        print(response)
