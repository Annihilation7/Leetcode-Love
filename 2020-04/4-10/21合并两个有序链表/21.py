#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 21.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/10 11:03 下午
#  Description : easy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        dummy_head = ListNode(-1)
        pre = dummy_head

        while cur1 or cur2:
            if not cur1:
                pre.next = cur2
                cur2 = cur2.next
            elif not cur2:
                pre.next = cur1
                cur1 = cur1.next
            elif cur1.val <= cur2.val:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next

        return dummy_head.next