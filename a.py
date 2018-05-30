#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
# 注意：项目中尽量不要出现循环嵌套  1000^3 = 1000000000次  假如1s = 100次

# 192秒
# begin_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a+b+c == 1000 and a*a+b*b == c*c:
#                 print(a, b, c)
# end_time = time.time()
# print("耗时:", end_time-begin_time)


# 30秒
# begin_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001-a):
#         for c in range(0, 1001-a-b):
#             if a+b+c == 1000 and a*a+b*b == c*c:
#                 print(a, b, c)
# end_time = time.time()
# print("耗时:", end_time-begin_time)


# 0.2秒
begin_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a*a+b*b == c*c:
            print(a, b, c)
end_time = time.time()
print("耗时:", end_time-begin_time)


# 一个算法的好坏从 时间 和 空间 来衡量
# 时间复杂度  空间复杂度

# 192秒   时间复杂度 O(n^3)
# 30秒    时间复杂度 O(n^3)
# 0.2秒  时间复杂度 O(n^2)


# 算法完成工作最少需要多少基本操作，即最优时间复杂度
# 算法完成工作最多需要多少基本操作，即最坏时间复杂度
# 算法完成工作平均需要多少基本操作，即平均时间复杂度

# [1, 3, 5, 7, 9]  按照升序排列 最优时间复杂度
# [9, 7, 5, 3, 1]  按照升序排列 最坏时间复杂度
# [9, 5, 7, 1, 3]  按照升序排列 平均时间复杂度


# [9, 7, 5, 3, 1]  ===>  [1, 3, 5, 7, 9]  排序四次，比较10次

# 程序 = 算法 + 数据结构