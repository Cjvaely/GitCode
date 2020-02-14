#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-23  16:54
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : DrawCircle.py
# @Version : 1.0
"""
画圈圈 填整数
1号转弯线：行+列 = n-1
2号转弯线：行=列
3号转弯线：行=列-1
"""
if __name__ == '__main__':
    SIZE = 7
    array = [[0] * SIZE]
    # 创建一个长度为SIZE * SIZE的二维列表
    for i in range(SIZE - 1):
        array += [[0] * SIZE]
    # orient表示绕圈的方向
    # 其中0表示向下，1表示向右，2表示向左，3表示向上
    orient = 0
    # 控制将1~SIZE * SIZE的数值填入二维列表中
    # j表示行，k表示列
    j = 0
    k = 0
    for i in range(1, SIZE * SIZE + 1):
        array[j][k] = i
        # 如果位于1号转弯线
        if j + k == SIZE - 1:
            # j > k，位于左下角
            if j > k:
                orient = 1
            # 位于右下角
            else:
                orient = 2
        # 如果位于2号线
        elif (k == j) and (k >= SIZE / 2):
            orient = 3
        elif (j == k - 1) and (k <= SIZE / 2):
            orient = 0
        # 根据方向来控制行索引、列索引的改变
        # 如果方向为向下绕圈
        if orient == 0:
            j += 1
        # 如果方向为向右绕圈
        elif orient == 1:
            k += 1
        elif orient == 2:
            k -= 1
        elif orient == 3:
            j -= 1
    # 采用遍历输出上面的二维列表
    for i in range(SIZE):
        for j in range(SIZE):
            print("%02d" % array[i][j], end = " ")
        print("")