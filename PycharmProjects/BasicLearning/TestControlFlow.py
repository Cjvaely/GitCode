#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-11  21:41
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : TestControlFlow.py
# @Version :1.0
"""
《Python疯狂讲义》 4 流程控制
"""
if __name__ == '__main__':

    # 4.3 断言
    """
    断言语句用于对一个bool表达式进行断言；
    如果表达式是true 则程序可以向下执行，否则引发AssertionError
    """
    # s_age = input("请输入您的年龄：")
    # age = int(s_age)
    # assert 20 < age < 80
    # print("您输入的年龄在20和80之间")

    # 4.4 循环结构
    """
    1.初始化语句
    2.循环条件
    3.循环体
    4.迭代语句
    """
    # 4.4.1 while循环
    # 循环初始化语句
    count_i = 0
    # 当count_i<10时，执行循环体
    # while count_i < 10:
    #     print("count_i: ", count_i)
    #     # 迭代语句
    #     count_i += 1
    # 循环结束
    # print("循环结束！")

    # 小程序：能整除3的放一个列表；不能的放另一个
    src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
    a_list = []     # 保存整除3的元素
    b_lsit = []     # 保存除以3余1的整数
    c_lsit = []     # 保存除以3余2的整数
    # 只要src_list还有元素，就继续循环
    while len(src_list) > 0:
        ele = src_list.pop()
        if ele % 3 == 0:
            a_list.append(ele)
        elif ele % 3 == 1:
            b_lsit.append(ele)
        else:
            c_lsit.append(ele)
    print("整除3:\t", a_list)
    print("除3余1:\t", b_lsit)
    print("除3余2:\t", c_lsit)
    """
    整除3:	 [24, 45, 12]
    除3余1:	 [109, 100, 13, 34]
    除3余2:	 [74, 56]
    """

    # 4.4.3 for-in循环
    """
    格式：
    for var in string|range|set:
        statements
    1.其中var受for-in控制，不能在循环中对该变量赋值
    2.可用与任何可迭代对象，即对象中包含一个_iter_方法，方法返回对象具有next()方法
    """
    # for-in计算阶乘
    # s_max = input("输入您想计算的阶乘: \n")
    # mx  =int(s_max)
    # result = 1
    # for num in range(1, mx + 1):
    #     result *= num
    # print("阶乘结果: ", result)

    # 4.4.5 使用for-in循环遍历字典
    print("\n")
    my_dict = {'语文': 89, '数学': 92, '英语': 80}
    # 通过items()方法遍历所有key-value
    # 由于返回的列表元素是key-value键值对，因此需要两个变量，应用了序列解包
    for key, value in my_dict.items():
        print("key:\t", key)
        print("value:\t", value)

    # 通过keys()遍历所有的key
    print("\n")
    for key in my_dict.keys():
        print("key:\t", key)

    # 通过values()遍历所有的value
    print("\n")
    for value in my_dict.values():
        print("value:\t", value)

    """
    实现一个程序：统计列表中各个元素出现的次数。
    可以考虑使用一个字典，列表的元素为key，次数为value。
    """
    src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4]
    statistics = {}
    # for ele in src_list:
    #     # 如果字典中包含ele代表的key
    #     if ele in statistics:
    #         statistics[ele] += 1
    #     # 如果字典中不包含ele代表的key
    #     else:
    #         statistics[ele] = 1
    # # 遍历dict,打印各元素次数
    # for ele, count in statistics.items():
    #     print("%s 出现的次数: %s\t" % (ele, count))

    # 优化后的方法：
    for ele in src_list:
        # 利用get()方法,如果指定key不存在，返回默认值
        statistics[ele] = statistics.get(ele, 0) + 1
    for ele, count in statistics.items():
        print("%s 出现的次数: %s\t" % (ele, count))

    # 4.4.6 循环使用else
    count_i = 0
    while count_i < 5:
        print("count_i < 5: ", count_i)
        count_i += 1
    else:
        print("count_i >= 5: ", count_i)
    """
    count_i < 5:  0
    count_i < 5:  1
    count_i < 5:  2
    count_i < 5:  3
    count_i < 5:  4
    count_i >= 5:  5
    """

    # 4.4.8 for表达式
    """
    for表达式用于利用其他区间，元组，列表等可迭代对象创建新的列表，格式：
    [表达式 for 循环计数器 in 可迭代对象]
    for表达式最终返回的是列表
    """
    a_range = range(10)
    # 对a_range执行for表达式
    a_list = [x * x for x in a_range]
    # a_list集合包含10个元素
    print(a_list)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 还可以添加if条件
    b_lsit = [x * x for x in a_range if x % 2 ==0]
    print(b_lsit)   # [0, 4, 16, 36, 64]

    # 如果将for表达式方括号改为圆括号，则生成一个生成器（generator）
    # 使用for表达式创建生成器
    c_generator = (x * x for x in a_range if x % 2 ==0)
    # 使用for循环迭代生成器
    for i in c_generator:
        print(i, end='\t')
    print()  # 0	4	16	36	64

    # for表达式可以用多个for
    d_list = [(x, y) for x in range(5) for y in range(4)]
    print(d_list)
    # [(0, 0), (0, 1), (0, 2), (0, 3),
    # (1, 0), (1, 1), (1, 2), (1, 3),
    # (2, 0), (2, 1), (2, 2), (2, 3),
    # (3, 0), (3, 1),(3, 2), (3, 3),
    # (4, 0), (4, 1), (4, 2), (4, 3)]

    # 多个for表达式可以使用if
    src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
    src_b = [3, 5, 7, 11]
    # 只要y能整除x，就将它们配对在一起
    result = [(x, y) for x in src_b for y in src_a if y % x == 0]
    print(result)   # [(3, 30), (3, 12), (3, 66), (3, 39), (3, 78), (3, 36), (3, 57), (5, 30), (11, 66), (11, 121)]

    # 4.4.9 常用的工具函数
    """
    zip()函数 可以将两个列表压缩成一个zip对象（可迭代），
    这样就可以使用一个循环遍历两个列表；
    zip对象包含的是原列表元素组成的元组；
    如果两个列表长短不一，以短的长度为主；
    压缩N个列表，则zip对象中的元素就是长度为N的元组
    """
    # 测试一下
    print("\n")
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    print([x for x in zip(a, b)])   # [('a', 1), ('b', 2), ('c', 3)]

    # zip实现并行遍历
    print("\n")
    books = ['crazy python', 'crazy swift', 'crazy kotlin']
    price = [79, 69, 89]
    # 使用zip压缩，实现并行遍历
    for book, price in zip(books, price):
        print("%s的价格是: %d" % (book, price))
    """
    crazy python的价格是: 79
    crazy swift的价格是: 69
    crazy kotlin的价格是: 89
    """

    # reversed()函数：接收各种序列，返回"反序排列"迭代器
    # 测试
    print("\n")
    a = range(10)
    print([x for x in reversed(a)])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # 并没有改变原对象a
    print([x for x in a])   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 不影响字符串本身，对字符串进行反序遍历
    c = 'Hello, Charil'
    print([x for x in reversed(c)])     # ['l', 'i', 'r', 'a', 'h', 'C', ' ', ',', 'o', 'l', 'l', 'e', 'H']

    """
    sorted()函数：接收一个可迭代对象作为参数，返回排序的列表
    """
    a = [20, 30, -1.2, 3.5, 90, 3.6]
    print(sorted(a))    # [-1.2, 3.5, 3.6, 20, 30, 90]
    # 不改变原来的对象
    print(a)    # [20, 30, -1.2, 3.5, 90, 3.6]
    # 添加reverse=True 从大到小
    print(sorted(a, reverse=True))  # [90, 30, 20, 3.6, 3.5, -1.2]
    # 还可以指定key参数，指定一个函数来生成排序的关键值，例如字符串长度
    my_list = ['fkit', 'carzyit', 'Cjv', 'python', 'javascript']
    print(sorted(my_list, key=len))     # ['Cjv', 'fkit', 'python', 'carzyit', 'javascript']