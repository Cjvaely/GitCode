#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-10  19:45
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : TestList.py
# @Version : 1.0
"""
《Python疯狂讲义》 3.3 使用列表
"""
if __name__ == '__main__':
    # 3.3.1 创建列表
    """
    Python提供list()创建列表, tuple()创建元组，可用于将列表、区间转化为元组
    """
    # 将元组转换为列表
    a_tuple = ('play', 20, -1.2)
    a_list = list(a_tuple)
    print(a_list)   # ['play', 20, -1.2]
    # 使用range创建区间（range）对象
    a_range = range(1, 5)
    print(a_range)  # range(1, 5)
    print(type(a_range))    # <class 'range'>
    # 区间转换成列表
    b_list = list(a_range)
    print(b_list)   # [1, 2, 3, 4]
    # 创建区间，指定步长
    print(list(range(4, 20, 3)))    # [4, 7, 10, 13, 16, 19]

    # 3.3.2 增加列表元素
    """
    append()用于增加元素，
    可以接收单个值、元组、列表，可能会形成嵌套列表、嵌套元组
    """
    c_list = ['crazy', 20, -2, 'python']
    # 追加元素
    print(c_list)   # ['crazy', 20, -2, 'python']
    # 追加元组
    b_tuple = (3.4, 6.28)
    c_list.append(b_tuple)
    print(c_list)   # ['crazy', 20, -2, 'python', (3.4, 6.28)]
    # 追加列表，把列表当做一个元素
    c_list.append(['a', 'b'])
    print(c_list)   # ['crazy', 20, -2, 'python', (3.4, 6.28), ['a', 'b']]
    # 追加元组中的元素
    d_list = [3.14, -2]
    d_list.extend((10, 3.14))
    print(d_list)   # [3.14, -2, 10, 3.14]
    # 追加列表中的元素
    d_list.extend([100, 34])
    print(d_list)  # [3.14, -2, 10, 3.14, 100, 34]

    # insert()可以向列表中间插入元素
    e_list = list(range(1, 6))
    print(e_list)   # [1, 2, 3, 4, 5]
    # 在索引3处插入字符串
    e_list.insert(3, "Python")
    print(e_list)   # [1, 2, 3, 'Python', 4, 5]
    # 在3处插入元组
    e_list.insert(3, tuple('Python'))
    print(e_list)   # [1, 2, 3, ('P', 'y', 't', 'h', 'o', 'n'), 'Python', 4, 5]

    # 3.3.3 删除列表元素
    """
    del 语句 不止可以删除列表元素，还能删除变量
    remove()方法删除列表元素，只删除第一个，如果找不到，引发ValueError错误
    clear()方法用于清空列表所有元素
    """
    f_list = ['python', 'java', 20, 45, (3, 4), [45, 'php']]
    # 删除第3个元素
    del f_list[2]
    print(f_list)   # ['python', 'java', 45, (3, 4), [45, 'php']]
    # 删除第3个到倒数第2个（不包含）,间隔为2
    del f_list[2:-2:2]
    print(f_list)   # ['python', 'java', (3, 4), [45, 'php']]

    g_list = [2, 4, -2, 'crazy', 2]
    # remove()删除第一次找到的2
    g_list.remove(2)
    print(g_list)   # [4, -2, 'crazy', 2]
    # clear清空元素
    g_list.clear()
    print(g_list)   # []

    # 3.3.5 列表其他用法
    """
    count()：统计列表中某个元素出现的次数
    index()：判断某个元素在列表中的位置
    pop()：出栈
    reverse()：将列表元素反向存放
    sort()：对列表元素排序
    """
    g_list = [2, 30, 'a', [5, 30], 30]
    # count用法 计算30出现的次数
    print(g_list.count(30)) # 2
    # index用法
    print(g_list.index(30)) # 1
    # pop用法
    print(g_list.pop()) # 30
    # reverse() 用法
    g_list.reverse()
    print(g_list)   # [[5, 30], 'a', 30, 2]
    # sort用法
    h_list = [1, 2, 7, -2, 5, 14, 8]
    # 从小到大排序
    h_list.sort()
    print(h_list)   # [-2, 1, 2, 5, 7, 8, 14]
    # 从大到小排序
    h_list.sort(key=len, reverse=True)
    print(h_list)