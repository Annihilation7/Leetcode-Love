#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 146
#  Author      : ZhenyuMa
#  Created     : 2020/4/1 9:42接雨水 下午
#  Description : hash table + 双向链表，跟着题解走一遍，思路很清晰


class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoubleList:
    def __init__(self):
        # self.head和self.tail都充当dummy节点（哨兵节点）
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self, x):
        """在最前面加个节点x，注意语句顺序，很经典！"""
        x.next = self.head.next
        x.prev = self.head
        self.head.next.prev = x
        self.head.next = x
        self.size += 1

    def remove(self, x):
        """删除节点x，调用这个函数说明x一定存在"""
        x.prev.next = x.next  # 像一个顺时针
        x.next.prev = x.prev
        self.size -= 1

    def removeLast(self):
        """
        删除链表中最后一个节点，并返回该节点
        注意双向链表的删除时间复杂度是O(1)的，因为立刻能找到该删除节点的前驱
        """
        if self.size == 0:
            return None
        last_node = self.tail.prev
        self.remove(last_node)
        return last_node

    def getSize(self):
        return self.size


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        val = self.map[key].val
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        new_item = Node(key, value)
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.addFirst(new_item)
            self.map[key] = new_item
        else:
            if self.capacity == self.cache.getSize():
                last_node = self.cache.removeLast()
                if last_node is not None:
                    self.map.pop(last_node.key)
            self.cache.addFirst(new_item)
            self.map[key] = new_item


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)