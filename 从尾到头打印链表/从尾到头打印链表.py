# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        if listNode != None:
            l.append(listNode.val)
            while listNode.next != None:
                l.insert(0, listNode.next.val)
                listNode = listNode.next
            return l
        else:
            return l