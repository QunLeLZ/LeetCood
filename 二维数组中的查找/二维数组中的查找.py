# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        col = len(array[0])-1
        row = 0
        while row <= (len(array)-1) and col >= 0:
            if target == array[row][col]:
                return True
            elif target < array[row][col]:
                col = col - 1
            else:
                row = row + 1
        return False