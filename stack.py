#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
stack：栈结构
特点：先进后出 FILO：first in last out
对应：进电梯 桶
功能：1.入栈   push
      2.出栈   pop
      3.获取栈顶元素
      4.获取栈大小
      5.判断栈是否为空


设有一个栈，元素一次进栈的顺序为A、B、C、D、E。下面_____C___是不可能的出站序列。

A.A、B、C、D、E
B.B、C、D、E、A
C.E、A、B、C、D
D.E、D、C、B、A
"""


class Stack(object):
    def __init__(self):
        # Python中不存在真正的私有方法。
        # 可以在类的方法或属性前加一个“_”单下划线，意味着该方法或属性不应该去调用
        # 并不是用来标识一个方法或属性是私有的，真正作用是用来避免子类覆盖其内容。
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self, value=None):
        if self.is_empty():
            raise IndexError("栈为空，不能删除")
        if not value:
            self.__stack.pop()
        else:
            while True:
                if self.__stack.pop() == value:
                    break

    def is_empty(self):
        # return True if len(self.__stack) == 0 else False
        return len(self.__stack) == 0

    def stack_size(self):
        return len(self.__stack)

    def top_stack(self):
        if self.is_empty():
            raise IndexError("栈为空，没有栈顶元素")
        return self.__stack.pop()

    # 尝试生成这样一个字符串，将其传给 eval()可重新生成同样的对象 ；
    # 否则，生成用尖括号包住的字符串，包含类型名和额外的信息(比如地址) ；
    # 一个类(class)可以通过 __repr__() 成员来控制repr()函数作用在其实例上时的行为。
    def __repr__(self):
        return "栈底"+"-->".join(self.__stack)+"栈顶" if not self.is_empty() else "空栈"

# 当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == '__main__':
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    # stack._Stack__stack = []
    stack.push('e')
    stack.push('f')
    print(stack)

    top = stack.top_stack()
    print(top)
    print(stack)

    stack.pop('c')
    print(stack)
    stack.pop('a')
    print(stack)
    print(stack)
    print(stack.stack_size())




