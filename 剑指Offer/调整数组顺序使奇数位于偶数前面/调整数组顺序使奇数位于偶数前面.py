# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        array1 = []
        l = len(array)
        for i in range(l):
            if array[l-i-1] % 2 != 0:
                array1.insert(0,array[-i-1])
            if array[i] % 2 == 0:
                array1.append(array[i])
        return array1