# """
# 使用单线程串行方式执行
# """
#
# import time
#
#
# def get_page(str):
#     print('正在下载：', str)
#     time.sleep(2)
#     print('下载成功：', str)
#
#
# name_list = ['xiaozi', 'aa', 'bb', 'cc']
# start_time = time.time()
#
# for name in name_list:
#     get_page(name)
#
# end_time = time.time()
# print('{}'.format(end_time - start_time))  # 8.03s

"""
使用线程池方式执行
"""

import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool

start_time = time.time()


def get_page(str):
    print('正在下载：', str)
    time.sleep(2)
    print('下载成功：', str)


name_list = ['xiaozi', 'aa', 'bb', 'cc']

# 实例化一个线程池对象
pool = Pool(4)
# map的作用是将name_list中的每一个元素传递给给get_page进行处理
# map的返回值是一个列表，每一个元素是get_page的返回值
pool.map(get_page, name_list)

end_time = time.time()
print('{}'.format(end_time - start_time))  # 2.02s
