#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 19.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/9 9:33 下午
#  Description : 双指针的题


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left_node = head
        right_node = head

        while n:
            try:
                right_node = right_node.next
            except Exception:
                print('invalid input.')
                return None
            n -= 1

        if right_node is None:
            ret_node = head.next
            head.next = None
            return ret_node

        while right_node.next:
            right_node = right_node.next
            left_node = left_node.next

        del_node = left_node.next
        left_node.next = del_node.next
        del_node.next = None  # 便于回收

        return head


