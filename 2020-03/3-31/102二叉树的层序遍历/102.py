#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 102
#  Author      : ZhenyuMa
#  Created     : 2020/3/31 9:31 下午
#  Description : 经典二叉树的bfs


from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        res = []

        while len(q):
            length = len(q)
            tmp_res = []
            for i in range(length):
                pop_node = q.popleft()
                tmp_res.append(pop_node.val)
                if pop_node.left is not None:
                    q.append(pop_node.left)
                if pop_node.right is not None:
                    q.append(pop_node.right)
            res.append(tmp_res)

        return res

