import requests
import asyncio
import time

urls = ['http://127.0.0.1:5000/bobo',
        'http://127.0.0.1:5000/zs',
        'http://127.0.0.1:5000/ls']


async def get_page(url):
    print('正在下载：', url)
    # requests.get是基于同步的，必须使用基于异步的网络请求模块进行指定URL的请求发送
    # aiohttp:基于异步网络请求模块
    response = requests.get(url=url)  # 这个代码是基于同步代码的，无法实现异步操作
    print(response.text)
    print('下载完毕，', url)


start_time = time.time()

tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()
print("总耗时：", end_time - start_time)
