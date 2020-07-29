import asyncio


async def request(url):
    print('正在请求URL是：', url)
    print('请求成功，', url)
    return url


# 使用async修饰的函数，调用返回的是一个协程对象
c = request('www.baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到事件循环对象loop中， 然后启动loop
# loop.run_until_complete(c)

"""task的使用"""
# loop = asyncio.get_event_loop()
# # 基于loop创建一个task任务对象
# task = loop.create_task(c)
# print(task)
#
# loop.run_until_complete(task)
# print(task)

"""
future的使用
本质和task一样，不同点就是创建方式不一样
"""
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

"""
绑定回调
"""


def callback_func(task):
    # result（）返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
