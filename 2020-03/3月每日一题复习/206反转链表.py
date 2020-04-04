#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 206
#  Author      : ZhenyuMa
#  Created     : 2020/4/3 1:23 下午
#  Description : 迭代 % 递归


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """递归"""
        if head.next is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList1(self, head: ListNode) -> ListNode:
        """迭代"""
        if head is None:
            return head

        pre = None
        cur = head

        while cur is not None:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        return pre