# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        sta,mid,end = 0,0,len(rotateArray)-1
        while rotateArray[sta] >= rotateArray[end]:
            if end-sta == 1:
                mid = end
                break
            mid = (sta + end) // 2
            if rotateArray[sta] == rotateArray[mid] and rotateArray[end] == rotateArray[mid]:
                minnum = rotateArray[sta]
                for i in range(sta+1,end+1):
                    if minnum > rotateArray[i]:
                        minnum = rotateArray[i]
                return minnum
            if rotateArray[sta] <= rotateArray[mid]:
                sta = mid
            elif rotateArray[end] >= rotateArray[mid]:
                end = mid
        return rotateArray[mid]