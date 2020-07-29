import asyncio
import time


async def request(url):
    print('正在下载：', url)
    # 在异步协程中如果出现了同步模块相关代码,那么就无法实现异步
    # time.sleep(2) # 同步代码
    # 当在asyncio中遇到阻塞操作，必须进行手动挂起
    await asyncio.sleep(2)  # 异步代码
    print('下载结束，', url)


start_time = time.time()
urls = ['www.baidu.com',
        'www.tencent.com',
        'www.jd.com'
        ]

# 任务列表：存放多个任务对象
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()
print(end_time - start_time)
