# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        hashMap = {}
        for i in array:
            if str(i) in hashMap:
                hashMap[str(i)] += 1
            else:
                hashMap[str(i)] = 1
        res = []
        for k in hashMap.keys():
            if hashMap[k] == 1:
                res.append(int(k))
                if len(res) == 2:
                    return res