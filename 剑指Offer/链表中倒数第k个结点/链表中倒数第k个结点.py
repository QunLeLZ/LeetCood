# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        p1 = head
        p2 = head
        while k > 1:
            if p2.next != None:
                p2 = p2.next
                k -= 1
            else:
                return None
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        return p1