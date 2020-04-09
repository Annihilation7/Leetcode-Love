#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 2.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/9 9:02 下午
#  Description : 炒鸡简单


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2

        dummy_head = ListNode(-1)
        pre = dummy_head
        c = 0

        while cur1 or cur2:
            num1 = cur1.val if cur1 else 0
            num2 = cur2.val if cur2 else 0
            _sum = num1 + num2 + c
            true_sum = _sum % 10
            c = _sum // 10
            pre.next = ListNode(true_sum)

            pre = pre.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        # 考虑最后可能有进位
        if c:
            pre.next = ListNode(c)

        return dummy_head.next