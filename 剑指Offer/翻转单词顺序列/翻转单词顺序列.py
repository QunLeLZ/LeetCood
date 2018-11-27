# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join(s.split()[::-1]) if s.strip() != "" else s