#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-10  13:29
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : TestString.py
# @Version : 1.0


"""
《Python疯狂讲义》2.4 字符串入门 + 《Python从入门到实践》
"""
if __name__ == '__main__':
    # 1. 使用方法修改字符串的大小写
    name = "chen cjv"
    # title是以首字母大写的方式显示每个单词
    print(name.title())  # Chen Cjv

    # 2. 合并(拼接)字符串
    first_name = "ada"
    last_name = "lovelace"
    full_name = first_name + " " + last_name
    print(full_name.title())

    # 3. 删除字符串末尾空白：rstrip()
    favorite_language = 'python '
    print(favorite_language.rstrip())
    # 删除左边空白：lstrip()   删除右边空白：strip()
    # Python2中，无需将要打印的内容放在括号内，类似于print "Hello Python 2.7 world!"

    # 4. 转换为字符串
    price = 2.3
    # 使用str()   python内置方法
    print(str(price))  # 2.3
    # 使用repr()
    print(repr(price))  # 2.3

    # 2.4.4 获取用户输入
    """
    input()函数用于向用户生成一条提示，获取输入的内容，总是返回一个字符串
    """
    # msg = input("请输入你的值：")
    # print(type(msg))    # <class 'str'>
    # print(msg)  # 123


    # 2.5.3 序列相关方法
    # 切片 获取一段字符串
    s = "I love Python"
    # 获取s中[3, 5)的字符串
    print(s[3:5])   # ov
    # 获取从3到倒数第5个(不包含)
    print(s[3:-5])  # ove P
    # in运算符，判断是否包含某个子串
    print('love' in s)  # True
    # 内置len()函数，输出s的长度
    print(len(s))   # 13
    # 全局内置min max获取字符串中最小字符和最大字符
    print(max(s))   # y
    print(min(s))   # 空格

    # title()将单词首字母大写
    # lower()将整个字符串改为小写
    # upper()将整个字符串改为大写
    a1 = 'our domin is Crazy.org'
    print(a1.title())
    print(a1.lower())
    print(a1.upper())
    """
    Our Domin Is Crazy.Org
    our domin is crazy.org
    OUR DOMIN IS CRAZY.ORG
    """

    # 2.5.7 分割、连接
    """
    split()：将字符串按指定分割符分割
    joint():将多个短语连接成字符串
    """
    s_j = "crazy in learning python.com"
    # 空白字符分割
    print(s_j.split())  # ['crazy', 'in', 'learning', 'python.com']
    # 空白字符分割，最多分割两个
    print(s_j.split(None, 2))   # ['crazy', 'in', 'learning python.com']
    # 使用.分割
    print(s_j.split('.'))

    my_split = s_j.split()
    # 使用/连接短语
    print('/'.join(my_split))   # crazy/in/learning/python.com
    # 使用", "连接短语
    print(', '.join(my_split))   # crazy/in/learning/python.com



