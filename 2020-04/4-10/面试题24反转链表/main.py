#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : main.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/10 11:06 下午
#  Description : 迭代/递归


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 迭代
        pre = None
        cur = head

        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        return pre

    def reverseList1(self, head):

        # 递归
        if head is None or head.next is None:
            return head

        new_head = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return new_head