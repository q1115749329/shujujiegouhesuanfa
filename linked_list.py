#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" 
顺序表：在内存中分配固定长度的内存空间，所有元素按照顺序存储
    特点：数据内存空间连续
    缺点：存储大量数据时会浪费大量内存空间，插入元素比较麻烦，每插入一个元素需要移动大量数据，效率比较低
    优点：查找元素比较方便
    时间复杂度：O(1)
    对应：c_array c里的数组
链表：在内存中动态分配内存空间来存储数据
    特点：数据内存空间不连续
    优点：省内存，插入元素比较方便
    缺点：查找元素不方便
    时间复杂度：O(n)
链表有三种：单链表 双链表 循环链表
"""


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkList(object):
    def __init__(self):
        # 链表头指针
        self.__head = None

    def link_list_size(self):
        return len(self.traversal())

    def is_empty(self):
        return self.__head == None

    def search(self, value):
        list1 = self.traversal()
        return value in list1

    # traversal 遍历
    def traversal(self):
        head = self.__head
        list1 = []
        while head != None:
            list1.append(head.value)
            head = head.next
        return list1

    def insert(self, index, value):
        index = index - 1
        node = Node(value)
        if index < 0 :
            node.next = self.__head
            self.__head = node
            return True
        if index >= self.link_list_size():
            self.append(value)
            return True
        head = self.__head
        pos = 0
        while head.next != None:
            if pos == index:
                node.next = head.next
                head.next = node
                return True
            pos += 1
            head = head.next
        return False

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.__head = node
        else:
            head = self.__head
            while head.next != None:
                head = head.next
            head.next = node

    def delete(self, value):
        head = self.__head
        if self.search(value):
            while head != None:
                if self.__head.value == value:
                    self.__head = self.__head.next
                    return True
                if head.next and head.next.value == value:
                    head.next = head.next.next
                    return True
                head = head.next
            return False
        else:
            return False

    def __repr__(self):
        if self.is_empty():
            return "空链表"
        list1 = self.traversal()
        return "-->".join(list1)


if __name__ == '__main__':
    link = LinkList()
    # link.append("a")
    # link.append("b")
    # link.append("c")
    # result = link.insert(4, "e")
    # result = link.insert(10, "f")
    # result = link.insert(0, "g")
    # result = link.insert(2, "z")
    # print(link)
    # print(result)
    # print(link.traversal())
    # print(link.link_list_size())
    # print(link.search('a'))
    # print(link.search('n'))
    # print("----------------------------------")
    # print(link.delete('a'))
    # print(link.delete('g'))
    # print(link.delete('z'))
    # print(link.delete('b'))
    # print(link.delete('c'))
    # print(link.delete('e'))
    # print(link.delete('f'))
    # print(link)
    link.search('a')
    print(link)