#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 递归逆序一个栈
#  Author      : ZhenyuMa
#  Created     : 2020/3/31 12:15 上午
#  Description :

"""
需要两个递归函数来完成
1。删除栈底元素并返回删除的元素
2。利用1来实现一个逆序栈的递归函数
"""

class Solution:
    def reverse(self, stack):
        if len(stack) == 0:
            return []
        self._reverse(stack)
        return stack

    def _getAndRemoveLastElement(self, stack):
        """递归函数1"""
        result = stack.pop()  # result是当前栈的栈顶元素
        if len(stack) == 0:
            return result
        elem = self._getAndRemoveLastElement(stack)
        stack.append(result)
        return elem

    def _reverse(self, stack):
        """递归函数2"""
        if len(stack) == 0:
            return
        # 倒数第二次的时候栈底元素即为原先的栈顶元素！
        last_elem = self._getAndRemoveLastElement(stack)
        self._reverse(stack)
        stack.append(last_elem)


if __name__ == "__main__":
    test = Solution()
    print(test.reverse([1, 2, 3, 4, 5]))
