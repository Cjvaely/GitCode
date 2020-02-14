#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-11  16:19
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : TestDict.py
# @Version : 1.0
"""
《Python疯狂讲义》 3.4 使用字典
Python中字典相当于保存了两组数据
一组是关键数据，称为key；一组是通过key来访问，称为value。
字典中的key不允许重复。
"""
if __name__ == '__main__':
    # 3.4.2 创建字典
    """
    1. dict()函数用来创建字典，dict也是一种类型，Python中的字典类型。
    2. 也可以使用花括号创建字典
    """
    score = {'语文': 89, '数学': 92, '英语': 93}
    print(score)    # {'语文': 89, '数学': 92, '英语': 93}
    print(type(score))  # <class 'dict'>
    # 空的花括号表示空的dict
    empty_dict = {}
    print(empty_dict)   # {}
    # 使用元组作为dict的key
    dict2 = {(20, 30): 'good', 30: 'bad'}
    print(dict2)    # {(20, 30): 'good', 30: 'bad'}
    """
    元组可以是dict的key，但是列表不能，因为dic要求key是不可变类型
    使用dict()创建字典时，可以传入多个列表或元组作为key-value对。
    """
    vegetable = [('celery', 1.8), ('brocoli', 1.9), ('lettuce', 2.19)]
    # 创建包含3个key-value的字典
    dict3 = dict(vegetable)
    print(dict3)    # {'celery': 1.8, 'brocoli': 1.9, 'lettuce': 2.19}
    cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
    # 创建包含3个key-value的字典
    dict4 = dict(cars)
    print(dict4)    # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
    # 创建空的字典
    dict5 = dict()
    print(dict5)    # {}
    # 使用关键字创建字典
    dict6 = dict(spinach=1.39, cabbage=2.59)
    print(dict6)    # {'spinach': 1.39, 'cabbage': 2.59}

    # 3.4.3 字典的基本用法
    # 通过key访value
    print(score['语文'])  # 89
    # 对不存在的key赋值，就是添加一对key-value
    score['历史'] = 94
    score[92] = 5.7
    print(score)    # {'语文': 89, '数学': 92, '英语': 93, '历史': 94, 92: 5.7}
    # 删除字典中的key-value，使用del语句
    del score[92]
    print(score)    # {'语文': 89, '数学': 92, '英语': 93, '历史': 94}
    # 对dict中存在的key-value赋值，会覆盖value
    score['语文'] = 90
    score['数学'] = 100
    print(score)    # {'语文': 90, '数学': 100, '英语': 93, '历史': 94}
    # 使用in或not in判断字典是否包含指定的key
    print('语文' in score)    # True
    print('政治' in score)    # False

    # 3.4.4 字典常用方法
    """
    1.clear(): 用于清空字典左右的key-value
    2.get(): 根据key取value，当用[]取并不存在的key时，字典会引发KeyError，get()只会返回None
    3.update(): 可使用一个字典所包含的key-value对来更新已有的字典，原有的会被覆盖，没有的会添加
    4.items()、keys()、values分别获取字典中所有key-value、所有key、所有value
        依次返回dict_items dict_keys dict_values
    5.pop(): 获取指定key的value值，并删除这个key-value
    6.popitem(): 随机弹出字典一个key-value，实际总是弹出底层存储的最后一个key-value
    7.setdefault(): 根据key查value值，若存在key，直接返回对应的value，否则，返回默认值
    8.fromkeys(): 使用给定的多个key创建字典，默认值是None
    """
    # clear()
    code = {'python': 4.5, 'java': 4.6}
    code.clear()
    print(code)     # {}
    # get()
    print(score.get('语文'))  # 90
    print(score.get('政治'))  # None
    # update()
    code = {'python': 4.5, 'java': 4.6}
    code.update({'python': 5.0, 'C': 2.5})
    print(code) # {'python': 5.0, 'java': 4.6, 'C': 2.5}

    cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
    # items() 获取所有key-value
    ims = cars.items()
    print(type(ims))    # <class 'dict_items'>
    # 将dict_items转换成list
    print(list(ims))    # [('BMW', 8.5), ('BENS', 8.3), ('AUDI', 7.9)]
    # 访问第二个键值对
    print(list(ims)[1])  # ('BENS', 8.3)

    # keys()获取所有key,返回一个dict_keys对象
    kys = cars.keys()
    print(type(kys))    # <class 'dict_keys'>
    # 将dict_keys转换为列表
    print(list(kys))    # ['BMW', 'BENS', 'AUDI']
    # values()获取列表中所有value
    vals = cars.values()
    print(type(vals))   # <class 'dict_values'>
    # 将dict_values转换为列表
    print(list(vals))   # [8.5, 8.3, 7.9]

    # pop() 取value 删key-value
    print(cars.pop('AUDI'))  # 7.9
    print(cars)     # {'BMW': 8.5, 'BENS': 8.3}
    # popitem() 随机弹出字典一个key-value()
    cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
    print(cars.popitem())   # ('AUDI', 7.9)
    print(cars)     # ('AUDI', 7.9)

    # setdefault()
    cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
    # 设置默认值9.2
    print(cars.setdefault('PORSCHE', 9.2))  # 9.2
    print(cars)  # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9, 'PORSCHE': 9.2}

    # fromkeys()
    a_dict = dict.fromkeys(['a', 'b'])
    b_dict = dict.fromkeys(('c', 'd'))
    print(a_dict)   # {'a': None, 'b': None}
    print(b_dict)   # {'c': None, 'd': None}
    # 指定值
    c_dict = dict.fromkeys((13, 17), 'good')
    print(c_dict)   # {13: 'good', 17: 'good'}

    # 3.4.5 使用字典格式化字符串
    # 在字符串模板中使用key
    temp = '书名是：%(name)s, 价格是：%(price)010.2f, 出版社是：%(publish)s}'
    book = {'name': '疯狂Python讲义', 'price': 88.9, 'publish': '电子社'}
    # 使用字典为字符串模板中的key传入值
    print(temp % book)  # 书名是：疯狂Python讲义, 价格是：0000088.90, 出版社是：电子社}
    book = {'name': '疯狂Kotlin讲义', 'price': 78.9, 'publish': '电子社'}
    print(temp % book)  #  书名是：疯狂Kotlin讲义, 价格是：0000078.90, 出版社是：电子社}
