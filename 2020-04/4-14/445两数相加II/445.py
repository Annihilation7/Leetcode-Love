#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 445.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/14 10:03 下午
#  Description : 递归或者借助两个栈来实现，本次使用栈来实现


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = self._pull_stack(l1)
        stack2 = self._pull_stack(l2)
        pre = None

        c = 0
        while len(stack1) or len(stack2):
            val1 = stack1[-1] if len(stack1) else 0
            val2 = stack2[-1] if len(stack2) else 0
            _sum = val1 + val2 + c
            true_sum = _sum % 10
            c = _sum // 10
            new_node = ListNode(true_sum)  # 插入法，而非pre.next=Node(true_sum)
            new_node.next = pre
            pre = new_node
            if len(stack1):
                stack1.pop()
            if len(stack2):
                stack2.pop()
        if c == 1:
            new_node = ListNode(1)
            new_node.next = pre
            pre = new_node

        return pre

    def _pull_stack(self, head):
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
        return stack
