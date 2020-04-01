#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 138
#  Author      : ZhenyuMa
#  Created     : 2020/4/1 8:44 下午
#  Description : 可以哈希表做，也可以剑指offer中那么做，本文尝试剑指offer中的解法，空间复杂度为O(1)


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        # 先在每个Node的后面插一个一样的Node
        pre = head
        while pre is not None:
            new_node = Node(pre.val, pre.next)
            pre.next = new_node
            pre = pre.next.next

        # 复制random分支
        pre = head
        while pre is not None:
            if pre.random is not None:
                pre.next.random = pre.random.next
            pre = pre.next.next

        # 拆开两个链表并复原原链表
        pre = head
        new_head = pre.next
        while pre.next is not None:
            pre_next = pre.next
            pre.next = pre_next.next
            pre = pre_next

        return new_head
