#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 98.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/21 12:15 上午
#  Description : 小递归


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, None, None)

    def helper(self, root, lower, upper):
        if root is None:
            return True
        if lower is not None and root.val <= lower:
            return False
        if upper is not None and root.val >= upper:
            return False
        return self.helper(root.left, lower, root.val) and \
               self.helper(root.right, root.val, upper)