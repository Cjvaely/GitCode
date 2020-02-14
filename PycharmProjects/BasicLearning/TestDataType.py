#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-10  14:28
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : TestDataType.py
# @Version :1.0
"""
《Python疯狂讲义》2.3 数值类型
"""
if __name__ == '__main__':

    """
    2.3.1 整型
    Python会将大整数当成long类型
    """
    a = 9999999999
    print(a)

    # 支持空值（None）
    b = None
    print(b)

    # 整数类型有4种表现形式
    # 1. 十进制
    # 2. 二进制以0b或0B开头
    bin_value = 0b11
    print(bin_value)    # 3
    # 3. 八进制以0o或0O开头
    oct_value = 0o11
    print(oct_value)    # 9
    # 4. 十六进制以0x或0X开头
    hex_value = 0x11
    print(hex_value)    # 17

    # 可以加下划线增加数值的可读性
    one_million = 1_000_000
    print(one_million)  # 1000000


    """
    2.3.2 浮点型
    表示形式：
    1. 十进制 5.12
    2. 科学计数 5.12e2(5.12x10^2)
    只有浮点类型才能用科学计数 51200是整数，但是512E2是浮点数
    """
    print(str(512E2))   # 51200.0
    f2 = 5e3
    print(type(f2)) # <class 'float'> float类型


    """
    2.3.3 复数
    复数的虚部用j或J表示
    可以导入Python的cmath模块(c表示complex)
    """
    ac1 = 3 + 0.2j
    print(ac1)  # (3+0.2j)
    print(type(ac1))    # 输出复数类型:<class 'complex'>
    ac2 = 4 - 0.1j
    print(ac2)  # (4-0.1j)
    print(ac1 + ac2)    # (7+0.1j)
    # 导入cmath
    import cmath
    ac3 = cmath.sqrt(-1)
    print(ac3)  # 1j


