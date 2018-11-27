# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        start,end = 1,2
        while start < end:
            sum = (start + end) * (end - start + 1) / 2
            if sum == tsum:
                tmp = []
                for i in range(start,end+1):
                    tmp.append(i)
                result.append(tmp)
                start += 1
            elif sum < tsum:
                end += 1
            else:
                start += 1
        return result