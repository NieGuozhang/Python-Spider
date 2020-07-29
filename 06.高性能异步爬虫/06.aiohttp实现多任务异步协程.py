"""
环境安装：pip install aiohttp

使用该模块中的ClientSession
"""
import asyncio
import time
import aiohttp

urls = ['http://127.0.0.1:5000/bobo',
        'http://127.0.0.1:5000/zs',
        'http://127.0.0.1:5000/ls']


# 异步请求
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # get()、post():
        # headers, params/data, proxy='http://ip:port'
        async with await session.get(url=url) as response:
            # text()方法返回字符串形式的响应数据
            # read()返回的是二进制形式的响应数据
            # json()返回的是json对象
            # 注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)


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
