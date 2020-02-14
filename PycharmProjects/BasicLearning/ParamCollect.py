#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-13  16:14
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : ParamCollect.py
# @Version : 1.0
"""
5.2.3参数收集（个数可变的参数）
Python允许在形参前面添加一个*号 允许传入多个参数
多个参数值被当成元组传入

"""
# 定义了支持参数收集的函数
def test(a, *books):
    print(books)
    # books 被当成元组处理
    for b in books:
        print(b)
    # 输出整数变量a的值
    print(a)


# test(5, "疯狂iOS讲义", "疯狂Java讲义")


"""
Python允许个数可变的形参处于形参列表的任意位置，
但要求一个函数只能带一个支持"普通"参数收集的形参
"""
def test2(*books, num):
    print(books)
    for b in books:
        print(b)

# test2("疯狂iOS讲义", "疯狂Java讲义", num=520)


"""
Python还可以收集关键字参数成字典，此时需要添加两个**
此时，一个函数可以同时包含一个支持"普通"参数收集的参数，和一个支持关键字参数收集的参数
"""
def test3(x, y, z=3, *books, **score):
    print(x, y, z)
    print(books)
    print(score)

# test3(1, 2, 3, "疯狂iOS讲义", "疯狂Java讲义", 语文=89, 数学=94)

"""
输出：
1 2 3
('疯狂iOS讲义', '疯狂Java讲义')
{'语文': 89, '数学': 94}
"""

# 上述test3()中z的默认值几乎不起作用，例如：
# test3(1, 2, "疯狂iOS讲义", "疯狂Java讲义", 语文=89, 数学=94)
"""
输出：
1 2 疯狂iOS讲义
('疯狂Java讲义',)
{'语文': 89, '数学': 94}
"""

"""
5.2.4 逆向参数收集：
程序已有列表、元组、字典等对象的前提下，把元素"拆开后"传给函数的参数
"""
def test4(name, message):
    print("用户是：", name)
    print("欢迎消息：", message)
my_list = ["孙悟空", "欢迎来我家！"]
# test4(*my_list)
"""
输出：
用户是： 孙悟空
欢迎消息： 欢迎来我家！
"""

"""
事实上，支持收集的参数，如果程序需要将一个元组传给该参数，还是要使用逆向收集
"""
def foo(name, *nums):
    print("name 参数: ", name)
    print("nums 参数: ", nums)

my_tuple = (1, 2, 3)
# 使用逆向收集，将my_tuple元组的元素传给nums参数
# foo('fkit', *my_tuple)
"""
输出：
name 参数:  fkit
nums 参数:  (1, 2, 3)
"""
# foo('fkit', my_tuple)
"""
输出：
name 参数:  fkit
nums 参数:  ((1, 2, 3),)
"""
# foo(*my_tuple)
"""
name 参数:  1
nums 参数:  (2, 3)
"""
# 不使用逆向收集（参数前不加*），整个元组会作为一个参数，
# 而不是将元组的元素作为多个参数
foo(my_tuple)
"""
输出：
name 参数:  (1, 2, 3)
nums 参数:  ()
"""


"""
字典也支持逆向收集，字典会以关键字的形式传入
"""
def bar(book, price, desc):
    print(book, "这本书的价格是：", price)
    print("描述信息", desc)


my_dict = {'price': 89, 'book': '疯狂Python讲义', 'desc': '这是一本系统全面的Python学习图书'}
# 按逆向收集的方式将my_dict的多个key-value对传给bar()函数
bar(**my_dict)
"""
输出：
疯狂Python讲义 这本书的价格是： 89
描述信息 这是一本系统全面的Python学习图书
"""
