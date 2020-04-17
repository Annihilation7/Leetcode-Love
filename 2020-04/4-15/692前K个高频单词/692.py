#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 692.py
#  Author      : ZhenyuMa
#  Created     : 2020-04-15 22:06
#  Description : 堆/partition，本题用最小堆来实现，这样时间复杂度是O(nlogk)的


from typing import List


class Data:
    def __init__(self, word, frequency):
        self._word = word
        self._frequency = frequency

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency < other.frequency
        return self.word > other.word  # 注意频率相同要按字典序排序，而我最终是从后往前塞元素的，所以要改成>

    def __gt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        return self.word < other.word

    @property
    def word(self):
        return self._word

    @property
    def frequency(self):
        return self._frequency


class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.size = 0

    def add(self, elem):
        """elem format: Data object"""
        if self.size < self.capacity:
            self.data.append(elem)
            self._shiftUp(len(self.data) - 1)
            self.size += 1
        elif elem > self.data[0]:
            self.data[0] = elem
            self._shiftDown(0)

    def removeMin(self):
        assert self.size > 0
        self._swap(0, self.size - 1)
        ret = self.data.pop().word
        self.size -= 1
        self._shiftDown(0)
        return ret

    def _left_child(self, idx):
        return idx * 2 + 1

    def _right_child(self, idx):
        return idx * 2 + 2

    def _parent(self, idx):
        return (idx - 1) // 2

    def _shiftUp(self, idx):
        while idx > 0:
            parent_idx = self._parent(idx)
            if self.data[parent_idx] < self.data[idx]:
                break
            self._swap(parent_idx, idx)
            idx = parent_idx

    def _shiftDown(self, idx):
        while self._left_child(idx) < self.size:
            j = self._left_child(idx)
            if j + 1 < self.size and self.data[j + 1] < self.data[j]:
                j += 1
            if self.data[idx] < self.data[j]:
                break
            self._swap(idx, j)
            idx = j

    def _swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        min_heap = MinHeap(k)

        record = {}
        for word in words:
            record[word] = record.get(word, 0) + 1

        for key, value in record.items():
            min_heap.add(Data(key, value))

        res = [None] * k
        for i in range(len(res) - 1, -1, -1):  # 从后往前塞元素
            res[i] = min_heap.removeMin()

        return res
