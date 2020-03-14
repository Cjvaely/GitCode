#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-08  15:05
# @Author  : Cjv
# @Site    : https://github.com/Cjvaely
# @File    : Vivo_test.py
# @Version :


#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
def solution(n):
    # write code here
    # 重点在于知道第n天每天生产多少
    sum = 0
    mid = n // 2
    larger = 0
    smaller = 1
    while mid > 1:
        for i in range(1, mid + 1):
            sum += i
        print(sum)  # 15  mid = 5
        print("larger={}".format(larger))
        print(mid)
        print(smaller)
        # 就是这里
        if sum == n:
            break
        # 如果此时，sum<n说明还没到分界
        elif sum < n:
            # 说明上一次sum>n 即mid < n < mid+1
            if larger:
                break   # 找到了分界点
            smaller, larger = 1, 0
            mid += 1
        else:
            # 说明上次偏小了，这次偏大了
            if smaller:
                mid -= 1
                break
            larger, smaller = 1, 0
            mid -= 1
    # 得到mid就是所需
    print(mid)
    sum = 0
    for i in range(mid + 1):
        sum += i * i
    print(sum)
    return sum + (n - ) * (mid + 1)

res = solution(11)
print(res)