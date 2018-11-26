# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr=[]
    def Insert(self, num):
        self.arr.append(num)
        self.arr.sort()
    def GetMedian(self,fuck):
        length=len(self.arr)
        return self.arr[length//2] if length%2==1 else (self.arr[length//2]+self.arr[length//2-1])/2.0