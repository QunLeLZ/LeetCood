# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        long = len(numbers)
        for i in range(len(numbers)):
            index = numbers[i]%long if numbers[i] >= long else numbers[i]
            if numbers[index] > long:
                duplication[0] = index
                return True
            numbers[index] += long
        return False
