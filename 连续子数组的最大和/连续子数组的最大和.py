# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max1 = max2 = array[0]
        for i in array[1:]:
            max1 = max(i,max1+i)
            max2 = max(max2,max1)
        return max2