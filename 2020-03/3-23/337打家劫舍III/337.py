

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        树形记忆化搜索
        当前节点选择偷：当前节点的钱 + 四个孙子节点的钱
        当前节点选择不偷：两个孩子节点的钱
        """
        self.record = {}
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return 0

        if root in self.record:
            return self.record[root]

        money1 = self.helper(root.left) + self.helper(root.right)

        money2_1 = money2_2 = 0
        if root.left is not None:
            money2_1 = self.helper(root.left.left) + self.helper(root.left.right)
        if root.right is not None:
            money2_2 = self.helper(root.right.right) + self.helper(root.right.left)
        money2 = money2_1 + money2_2 + root.val

        cur_res = max(money1, money2)
        self.record[root] = cur_res

        return cur_res