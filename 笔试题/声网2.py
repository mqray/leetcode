# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/14 9:38 PM
# 设计lru

class ListNode:
    def __init__(self,key,val):
        self.key = self.key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:
    def __init__(self,capacity):
        self.dic ={}
        self.head = ListNode(None,None)
        self.tail = ListNode(None,None)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self,key):
        if not key in self.dic:
            return -1
        node = self.dic.get(key)
        self.delete(node)
        self.set(node)#插入到最前面
        return node.val

    def delete(self,node):
        #双向链表删除
        node.pre.next,node.next.pre = node.next,node.pre

    def set(self,node):
        # 每次插入都插入到head后
        node.next, node.pre = self.head.next,self.head
        self.head.next = node
        tmp = node.next
        tmp.pre = node
        # self.dic还要加入


