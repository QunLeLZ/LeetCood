# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        pPre = None
        pCur = pHead
        pNext = None
        while pCur != None:
            if pCur.next != None and pCur.val == pCur.next.val:
                pNext = pCur.next
                while pNext.next != None and pNext.next.val == pCur.val:
                    pNext = pNext.next
                if pCur == pHead:
                    pHead = pNext.next
                else:
                    pPre.next = pNext.next
                pCur = pNext.next
            else:
                pPre = pCur
                pCur = pCur.next
        return pHead