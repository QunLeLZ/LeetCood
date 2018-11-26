# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        if len(num)>0 and size > 0:
            endP = size
            while endP <= len(num):
                res.append(max(num[endP-size:endP]))
                endP += 1
        return res