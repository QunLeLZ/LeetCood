# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        first,second,third = 1,2,0
        for i in range(2,number):
            third = first + second
            first,second = second,third
        return third