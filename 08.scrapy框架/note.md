# scrapy框架

## 什么是框架？
- 集成了很多功能并且具有很强通用性的一个项目模板

## 如何学习框架？
- 专门学习框架封装的各种功能的详细用法
- 后期深入框架低层源码细节

## 什么是scrapy?
- 爬虫中封装好的一个明星框架。功能：高性能的持久化存储，异步的数据下载，高性能的数据解析， 分布式

## scrapy框架的使用
- 环境安装：
    - Mac or Linux: `pip install scrapy`
- 创建一个工程
    - `scrapy startproject 工程名`
    - 在spiders子目录中创建一个爬虫文件
        - `cd 工程名`
        - `scrapy genspider spiderName www.xxx.com`
    - 执行工程
        - `scrapy crawl spiderName`
## scrapy数据解析

    