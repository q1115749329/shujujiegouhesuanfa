#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" 
冒泡排序：核心 交换 比较
[3,5,1,4,2,6]
第一次排序：
    [3,5,1,4,2,6]
    [3,1,5,4,2,6]
    [3,1,4,5,2,6]
    [3,1,4,2,5,6]
    [3,1,4,2,5,6]
第二次排序：
    [1,3,4,2,5,6]
    [1,3,4,2,5,6]
    [1,3,2,4,5,6]
    [1,3,2,4,5,6]
    [1,3,2,4,5,6]
    ....



最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
最坏时间复杂度：O(n2)
稳定性：稳定

"""
# list1 = [3, 5, 1, 4, 2, 6]
# for j in range(0, 6):
#     for i in range(0, len(list1)-j-1):
#         a1 = list1[i]
#         a2 = list1[i+1]
#         if a1 > a2:
#             list1[i],list1[i+1] = list1[i+1],list1[i]
#         print(list1)
#     print("---------------------")


alist = [3, 5, 5, 4, 2, 6]
for j in range(len(alist)-1,0,-1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
            print(alist)
        print("-----------------")

