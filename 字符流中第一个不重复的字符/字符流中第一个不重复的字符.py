# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.hashMap = {}
    def FirstAppearingOnce(self):
        # write code here
        length = len(self.s)
        for i in range(length):
            if self.hashMap[self.s[i]] == 1:
                return self.s[i]
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.hashMap:
            self.hashMap[char] = 1
        else:
            self.hashMap[char] += 1