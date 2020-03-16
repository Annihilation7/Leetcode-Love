

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """递归取判断每个节点就可以了"""

        # 同时到None，说明结构相同
        if p is None and q is None:
            return True

        if q is None or p is None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
