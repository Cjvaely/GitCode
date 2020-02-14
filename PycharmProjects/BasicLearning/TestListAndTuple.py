#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-10  17:26
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : TestListAndTuple.py
# @Version :1.0
"""
《Python疯狂讲义》 3.2 列表、元组通用用法
"""

if __name__ == '__main__':

    # 3.2.3 加法
    """
    加法是两个列表或元祖所包含元素的总和
    只能是元组 + 元组，列表 + 列表
    """
    a_tuple = ('uestc', 20, -1.2)
    b_tuple = (127, 'uestc', 'xr', 3.33)
    # 计算元祖相加
    sum_tuple = a_tuple + b_tuple
    print(sum_tuple)    # ('uestc', 20, -1.2, 127, 'uestc', 'xr', 3.33)
    print(a_tuple)  # ('uestc', 20, -1.2)
    print(b_tuple)  # (127, 'uestc', 'xr', 3.33)

    a_list = [20, 30, 50, 100]
    b_list = ['a', 'b', 'c']
    # 计算列表相加
    sum_list = a_list+ b_list
    print(sum_list)     # [20, 30, 50, 100, 'a', 'b', 'c']
    print(a_list + ['tc'])  # [20, 30, 50, 100, 'tc']

    # 3.2.4 乘法
    """
    列表和元组的乘法就是把它们包含的元素重复N次
    """
    # ('uestc', 20, -1.2, 'uestc', 20, -1.2, 'uestc', 20, -1.2)
    print(a_tuple * 3)
    # [20, 30, 50, 100, 20, 30, 50, 100, 20, 30, 50, 100]
    print(a_list * 3)

    # 同时对元组使用乘法、加法
    order_endings = ('st', 'nd', 'rd')\
        + ('th',) * 17 + ('st', 'nd', 'rd')\
        + ('th',) * 7 + ('st',)
    # 将会看到 st、nd、rd、17个th、st、nd、rd、7个th
    print(order_endings)
    # day = input("输入日期（1-31）:")
    # # 将字符串转化成整数
    # day_int = int(day)
    # print(day + order_endings[day_int - 1])

    # 3.2.5 in运算符
    """
    用于判断列表或元组中是否包含某个元素
    """
    in_tuple = ('car', 'bike', 'train')
    print('car' in in_tuple)    # True
    print('a' in in_tuple)  # False
    print('a' not in in_tuple)  # True

    # 3.2.6 长度、最大值、最小值
    # 元素都是数值的元组
    size_tuple = (20, 10, -2, 15.2, 102, 50)
    # 计算最大值
    print(max(size_tuple))  # 102
    # 计算最小值
    print(min(size_tuple))  # -2
    # 元组长度
    print(len(size_tuple))  # 6

    # 3.2.7 序列封包和解包
    """
    程序把多个值赋给一个变量时，Python自动封装成元组，这就是序列封包
    程序允许将序列（元组或列表）直接赋值给多个变量，这就是序列解包
    """
    # 封包
    vals = 10, 20, 30
    print(vals)     # (10, 20, 30)
    # 解包
    test_unseq = tuple(range(1, 10, 2))
    print(test_unseq)   # (1, 3, 5, 7, 9)
    a, b, c, d, e = test_unseq
    print(a, b, c, d, e)    # 1 3 5 7 9
    list_unseq = ['fkit', 'crazy']
    # 将list_unseq序列的元素依次赋值给a_str, b_str
    a_str, b_str = list_unseq
    print(a_str, b_str) # fkit crazy
    # 同时将多个值赋值给多个变量
    x, y, z = 10, 20, 30
    print(x, y, z)  # 10 20 30
    # 交换变量的值
    x, y, z = y, z, x
    print(x, y, z)  # 20 30 10
    # 序列解包也可以剩一部分
    # first、second保存前两个，剩下的存在rest
    first, second, *rest = range(10)
    print(first, second, rest)  # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
    *begin, last = range(1, 10)
    print(begin, last)  # [1, 2, 3, 4, 5, 6, 7, 8] 9
    first, *middle, last = range(1, 10)
    print(first, middle, last)  # 1 [2, 3, 4, 5, 6, 7, 8] 9