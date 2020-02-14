#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-11  23:13
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : Num_to_rmb.py
# @Version :1.0
"""
《Python疯狂讲义》 4.6 牛刀小试
"""
if __name__ == '__main__':
    # 4.6.1 数字转人民币
    """
    把一个浮点数分解成整数部分和小数部分字符串
    num是需要被分解的浮点数
    返回分解出来的整数部分和小数部分
    第一个数组元素是整数部分，第二个数组元素是小数部分
    """


    def divide(number):
        """
        :param number: 需要被分解的浮点数
        :return: 分解出来的整数部分和小数部分，第一个数组是整数部分，第二个是小数部分
        """
        # 将一个浮点数转换为整数
        integer = int(number)
        # 浮点数-整数，得到小数部分，小数部分乘以100，得到2位小数
        fraction = round((number - integer) * 100)
        # 把整数转为字符串
        return str(integer), str(fraction)

    han_list = ["零", "壹", "贰", "叁", "肆",
                "伍", "陆", "柒", "捌", "玖"]
    unit_list = ["十", "百", "千"]
    """
    把一个4位数数字符变成汉字字符
    """
    def four_to_hanstr(num_str):
        """
        :param num_str: 需要被转换的4位数字字符串
        :return: 4位数字字符串被转换成汉字字符串
        """
        result = ""
        num_len = len(num_str)
        # 依次遍历数字字符串的每一位数字
        for i in range(num_len):
            # 把字符串转换数值
            num = int(num_str[i])
            # 如果不是最后一位数字，而且数字不是0，则需要添加单位
            if i != num_len - 1 and num != 0:
                result += han_list[num] + unit_list[num_len - 2 - i]
                # 否则不要添加单位
            else:
                result += han_list[num]
        return result

    """
    把数字字符转换成汉字字符串
    """
    def integer_to_str(num_str):
        """
        :param num_str: 需要被转化的数字字符串
        :return: 数字字符串被转换成汉字字符串
        """
        str_len = len(num_str)
        if str_len > 12:
            print("数字太大，翻译不了")
            return
        # 如果大于八位，包含单位亿
        elif str_len > 8:
            return four_to_hanstr(num_str[:-8]) + "亿" + \
                four_to_hanstr(num_str[-8:-4]) + "万" + \
                four_to_hanstr(num_str[-4:])
        # 如果大于4位，包含单位"万"
        elif str_len > 4:
            return four_to_hanstr(num_str[:4]) + "万" + \
                four_to_hanstr(num_str[-4:])
        else:
            return four_to_hanstr(num_str)
    num = float(input("请输入一个浮点数："))
    # 测试把一个浮点数分解成整数部分和小数部分
    integer, fraction = divide(num)
    # 测试把一个4位数字字符串转成汉子字符串
    print(integer_to_str(integer))
    print(fraction)