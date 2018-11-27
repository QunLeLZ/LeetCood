# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        nodeStack=[pRoot]
        result=[]
        while nodeStack:
            res = []
            nextStack=[]
            for i in nodeStack:
                res.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            nodeStack=nextStack
            result.append(res)
        returnResult=[]
        for i,v in enumerate(result):
            if i%2==0:
                returnResult.append(v)
            else:
                returnResult.append(v[::-1])
        return returnResult