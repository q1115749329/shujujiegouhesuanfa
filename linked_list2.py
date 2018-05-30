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
        self.pre = None


class LinkList(object):
    def __init__(self):
        # 链表头指针
        self.__head = None

    def link_list_size(self):
        """
        返回列表长度
        :return:
        """
        # 通过遍历获取所有指针的值的列表
        list1 = self.traversal()
        # 返回列表长度
        return len(list1)

    def is_empty(self):
        """
        判断双链表是否为空，如果头指针为空则双链表为空
        :return: True表示为空
        """
        return self.__head == None

    def search(self, value):
        return value in self.traversal()

    # traversal 遍历
    def traversal(self):
        """
        遍历双链表的所有结点
        :return:
        """
        # 获得头指针
        head = self.__head
        # 创建空列表用来存放结点的值
        list1 = []
        # 通过循环让头指针后移，此时head表示当前结点
        while head != None:
            # 每获取一个指针的值就拼接到列表中
            list1.append(head.value)
            # 指针后移
            head = head.next
        # 返回列表
        return list1

    def insert(self, index, value):
        """
        往双链表中插入结点
        :param index:
        :param value:
        :return:
        """
        node = Node(value)
        # 在当前结点的前一个结点后边插入该节点
        index = index - 1
        # 如果在双链表的头部插入
        if index < 0:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node
            return True
        # 在双链表的尾部插入
        if index > self.link_list_size():
            head = self.__tail
            head.next = node
            node.pre = head
            return True
        # 在双链表的中间插入
        pos = 0
        head = self.__head
        while head.next != None:
            # 找到插入位置
            if pos == index:
                node.next = head.next
                head.next.pre = node
                head.next = node
                node.pre = head
                return True
            pos += 1
            head = head.next
        return False

    def append(self, value):
        """
        为双链表拼接结点
        :param value:
        :return:
        """
        node = Node(value)
        # 先判断双链表是否为空
        if self.is_empty():
            # 如过为空，头指针指向该结点
            self.__head = node
        else:
            # 如果不为空，先获得尾指针，然后拼接该结点
            head = self.__tail
            head.next = node
            node.pre = head

    def delete(self, value):
        """
        删除双链表中的结点
        :param value:
        :return:
        """
        # 如果删除的结点存在
        if self.search(value):
            head = self.__head
            while head.next != None:
                # 如果找到要删除的当前节点
                if head.value == value:
                    # 如果删除头节点
                    if self.__head == head:
                        self.__head = head.next
                        head.next.pre = None
                        head.next = None
                        return True
                    # 如果删除中间节点
                    head.pre.next = head.next
                    head.next.pre = head.pre
                    head.pre = None
                    head.next = None
                    return True
                head = head.next
            #  如果删除尾节点
            if self.__tail == head and head.value == value:
                head.pre.next = None
                head.pre = None
                return True
        return False

    @property
    def __tail(self):
        """
        定义一个尾指针，通过调用属性来模拟调用方法，通过property装饰器来实现
        :return:
        """
        head = self.__head
        while head.next != None:
            head = head.next
        return head

    def __repr__(self):
        if self.is_empty():
            return "空链表"
        list1 = self.traversal()
        return "<=>".join(list1)


if __name__ == '__main__':
    link = LinkList()
    link.append('a')
    link.append('b')
    link.append('c')
    print(link)
    print(link.traversal())
    link.insert(-1, 'T')
    link.insert(10, 'U')
    print(link)

    link.insert(2, 'P')
    print(link.insert(-20, 'P'))
    print(link)
    print("==================================")
    link.delete('U')
    print(link)
