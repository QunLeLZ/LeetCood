# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        zero,count = 0,0
        if not numbers:
            return False
        numbers.sort()
        for i in range(0,4):
            if numbers[i] == 0:
                zero += 1
                continue
            if numbers[i] == numbers[i+1]:
                return False
            count = count + numbers[i+1] - numbers[i] - 1
        if zero >= count:
            return True
        else:
            return False