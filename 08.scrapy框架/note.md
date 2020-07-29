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
- 可以直接由response采用xpath进行解析

## scrapy数据持久化存储
- 基于终端指令
    - 要求：只可以将parse方法的返回值存储到本地的文本文件中，所以需要parse方法有返回值
    - 注意：持久化存储文件对应的格式只能是：('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
    - 指令：` scrapy crawl XXX -o filePath`
    - 好处：简介高效便捷
    - 缺点：局限性比较强（数据只可以存储到指定后缀的文本文件中，不能存到数据库）
- **基于管道**（重点）
    - 编码流程
        - 
    