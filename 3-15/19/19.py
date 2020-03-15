

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        """
        两个指针，一个pre，一个cur。cur先走n-1步，然后两个指针一起走，直到
        cur的next为空的时候，pre的下一个就是要删除的倒数第n个节点。
        一次遍历
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head

        pre_node = dummy_head
        cur_node = pre_node.next

        while n - 1:
            cur_node = cur_node.next
            n -= 1

        while cur_node.next:
            cur_node = cur_node.next
            pre_node = pre_node.next

        del_node = pre_node.next
        pre_node.next = del_node.next
        del_node.next = None

        return dummy_head.next
