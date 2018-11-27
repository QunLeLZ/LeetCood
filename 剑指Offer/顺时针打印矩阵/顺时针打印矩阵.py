# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        l = []
        while matrix:
            l += matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    l.append(i.pop())
            if matrix:
                l += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for m in matrix[::-1]:
                    l.append(m.pop(0))
        return l