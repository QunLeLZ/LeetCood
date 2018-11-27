# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        q1 = [root]
        res = []
        while q1:
            q2 = []
            for i in q1:
                if i.left:
                    q2.append(i.left)
                if i.right:
                    q2.append(i.right)
                res.append(i.val)
            q1 = q2
        return res