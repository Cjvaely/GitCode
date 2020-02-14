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

    # 2.4.5 长字符串
    """
    三个引号就是长字符串，不仅可以用来注释，还能赋值给变量
    """
    s_long = '''"Let's go finishing", said Mary.
    "OK, Let's go", said her brother.
    They walked to a lake.'''
    print(s_long)

    # 还可以使用转义字符（\）不会中断字符
    s2 = 'The quick brown fox\
 jumps over the lazy dog'
    print(s2)  # The quick brown fox jumps over the lazy dog

    # 2.4.6 原始字符串
    # 原始字符串以r开头，不会把\当做特殊字符
    s1 = r"G:\Library"  # G:\Library
    print(s1)

    # 如果要在原始字符串加上\，除了使用长字符串，还可以：
    s3 = r'Good Python' '\\'  # 两个字符串会自动拼接
    print(s3)  # Good Python\

    # 2.4.7 字节串(bytes)
    """
    字节串是Python3新增，对应字符串，但是字节串以字节为单位进行操作
    bytes()对象只负责以为字节（二进制格式）序列记录数据，
    可以用于在网上传输数据，也可以存储二进制格式的文件，如图片、音频
    
    1. 字符串都是ASCII码，可以通过字符串前加b构建字节串值
    2. bytes()函数可将字符串按制定字符集转化成字节串，默认是utf-8
    3. 调用字符串本身的encode()方法可将字符串按制定字符集转换为字节串
    """
    # 创建一个空的bytes
    b1 = bytes()
    # 创建一个空的bytes值
    b2 = b''
    # 通过b前缀指定
    b3 = b'hello'
    print(b3)  # b'hello'
    print(b3[0])  # 104'
    print(b3[2:4])  # b'hello'
    # 调用bytes方法将字符串转成bytes对象
    b4 = bytes("I love python", encoding='utf-8')
    print(b4)  # b'I love python '
    # 利用encode()编码成bytes
    b5 = "I love python".encode('utf-8')
    print(b5)  # b'I love python'
    # 将bytes对象解码成字符串
    st = b5.decode('utf-8')
    print(st)  # I love python

    # 2.5.2 字符串格式化
    number = 108
    # %s是一个占位符，指定将变量使用str()函数转换为字符串
    print("the number of book is %s" % number)  # the number of book is 108
    user = "Charil"
    age = 8
    print("%s is a %d years old boy." % (user, age))

    num = -28
    # i和d表示十进制 o表示八进制 x表示十六进制 s表示字符串
    # 6表示最小宽度，默认是右对齐的，允许在宽度前加标志
    # -：左对齐
    # +：数值
    # 0：表示不补充空格，补充0
    # 三个标志可同时存在
    print("num is: %6i" % num)
    print("num is: %6d" % num)
    print("num is: %6o" % num)
    print("num is: %6x" % num)
    print("num is: %6s" % num)
    """
    num is:    -28
    num is:    -28
    num is:    -34
    num is:    -1c
    num is:    -28
    """
    num2 = 30
    # 最小宽度为0
    print("num2 is: %0d" % num2)
    # 最小宽度为6，左边补0
    print("num2 is: %06d" % num2)
    # 最小宽度为6，带+号
    print("num2 is: %+6d" % num2)
    # 最小宽度为6，左对齐
    print("num2 is: %-6d" % num2)
    """
    num2 is: 30
    num2 is: 000030
    num2 is:    +30
    num2 is: 30
    """
    # 对于浮点数：
    my_value = 3.1415926
    # 最小宽度为8，小数点后保留3位
    print("my value is: %8.3f" % my_value)
    # 最小宽度为8，小数点后保留3位，左边补0
    print("my value is: %08.3f" % my_value)
    # 最小宽度为8，小数点后保留3位，左边补0，带+号
    print("my value is: %+08.3f" % my_value)
    """
    my value is:    3.142
    my value is: 0003.142
    my value is: +003.142
    """

    the_name = "Charil"
    # 最小长度为0，保留3个字符
    print("the name is: %.3s" % the_name)
    # 最小长度为10，保留2个字符
    print("the name is: %10.2s" % the_name)
    """
    the name is: Cha
    the name is:         Ch
    """

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

    # 2.5.6 查找、替换
    """
    str还提供：
    1. startswith(self, prefix, start=None, end=None)
        若以prefix开头，返回True
    2. endswith(self, suffix, start=None, end=None)
        若以suffix结尾，返回True
    3. find(self, sub, start=None, end=None)
        查找sub子串在字符串中的位置，没找到返回-1
    4. index(self, sub, start=None, end=None)
        查找sub子串在字符串中的位置，没找到引发ValueError错误
    5. replace(self, *args, **kwargs)
        用子串替换字符串中的子串
    6. translate(self, *args, **kwargs)
        用给定的模板替换字符串的每个字母
    """
    print(a1.startswith('our'))   # True
    print(a1.endswith('Org'))   # False
    print(a1.find('Cjv'))   # -1
    print(a1.find('domin'))   # 4
    # 从5处开始找，出错
    # print(a1.index('cjv', 5))
    # 全部换
    print(a1.replace('o', 'TX'))    # TXur dTXmin is Crazy.TXrg
    # 换一个
    print(a1.replace('o', 'TX', 1))  # TXur domin is Crazy.org
    # 定义一个翻译映射表：a->α b->β t->τ
    tran = 'a b c d e f g aaa bbb ccc ttt'
    table = {97: 945, 98: 946, 116: 964}
    print(tran.translate(table))
    # 可以利用函数maketrans()制作映射表
    table = str.maketrans('abc', 'αβτ')
    print(table)    # {97: 945, 98: 946, 99: 964}

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



