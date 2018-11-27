# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        first,second,third = 1,2,0
        for i in range(2,number):
            third = first + second
            first,second = second,third
        return third