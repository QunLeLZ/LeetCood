# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        tree = TreeNode(pre[0])
        i = tin.index(pre[0])
        tree.left = self.reConstructBinaryTree(pre[1:i+1],tin[:i])
        tree.right = self.reConstructBinaryTree(pre[1+i:],tin[i+1:])
        return tree