# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    def push(self, node):
        # write code here
        self.arr.append(node)
    def pop(self):
        # write code here
        return self.arr.pop()
    def top(self):
        # write code here
        return self.arr[-1]
    def min(self):
        # write code here
        return min(self.arr)