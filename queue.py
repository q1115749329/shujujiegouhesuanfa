#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
队列：queue
特点：先进先出 FIFO first in first out
对应：排队买票 打印机 水管
队列和栈 成对出现
常用操作： 1.获得队列大小
           2.出队
           3.入队
           4.判断队是否为空
"""


class Queue(object):
    def __init__(self):
        self.__queue = []

    def q_size(self):
        return len(self.__queue)

    def is_empty(self):
        return len(self.__queue) == 0

    def l_push(self, value):
        self.__queue.insert(0, value)

    def r_push(self, value):
        self.__queue.append(value)

    def l_pop(self, value=None):
        if self.is_empty():
           raise IndexError("队列为空")
        if not value:
            self.__queue.pop(0)
        else:
            while True:
                if self.__queue.pop(0) == value:
                    break

    def r_pop(self, value=None):
        if self.is_empty():
           raise IndexError("队列为空")
        if not value:
            self.__queue.pop()
        else:
            while True:
                if self.__queue.pop() == value:
                    break

    def __repr__(self):
        return "--".join(self.__queue) if not self.is_empty() else "空列表"


if __name__ == '__main__':
    q = Queue()
    q.l_push('a')
    q.l_push('b')
    q.l_push('c')
    q.r_push('d')
    q.r_push('e')
    q.r_push('f')
    print(q)

    q.l_pop('b')
    q.r_pop('d')
    print(q)

