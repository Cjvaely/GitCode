#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-13  14:53
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : function_doc.py
# @Version : 1.0
"""
为函数提供文档
"""

if __name__ == '__main__':
    def my_max(x, y):
        '''
        :param x: 第一个数
        :param y: 第二个数
        :return: 获取两个数值之间较大的数
        '''
        # 定义一个变量z,该变量等于较大值
        z = x if x > y else y
        # 返回变量z的值
        return z


    # 使用help()函数查看my_max的帮助文档
    help(my_max)
    print(my_max.__doc__)