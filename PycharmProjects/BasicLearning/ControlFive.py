#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-01  15:53
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : ControlFive.py
# @Version : 1.0
"""
控制台五子棋
先定义一个二维列表作为棋盘，下一步棋，就是为而为二维列表赋值
"""
if __name__ == '__main__':
    # 定义棋盘大小
    BOARD_SIZE = 15
    # 定义一个二维列表
    board = []


    def initBoard():
        # 为每个元素赋值"+" 在控制台画出棋盘
        for i in range(BOARD_SIZE):
            row = ["+"] * BOARD_SIZE
            board.append(row)

    # 在控制台输出棋盘的方法
    def printBoard():
        # 打印每个列表元素
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # 打印列表元素后不换行
                print(board[i][j], end=" ")
            # 打印完一行元素后换行
            print()


    initBoard()
    printBoard()
    inputStr = input("请输入您下棋的坐标，以x,y格式：\n")
    while inputStr != None:
        # 将用户输入的字符串以逗号（，）作为分隔符，分隔成两个字符串
        x_str, y_str = inputStr.split(sep=",")
        # 为对应的列表元素赋值""