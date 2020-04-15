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
        return self.frequency <= other.frequency

    def __gt__(self, other):
        return self.frequency >= other.frequency

    @property
    def word(self):
        return self.word

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

    def _left_child(self, idx):
        return idx * 2 + 1

    def _right_child(self, idx):
        return idx * 2 + 2

    def _parent(self, idx):
        return (idx - 1) // 2

    def _shiftUp(self, idx):
        while idx > 0:
            parent_idx = self._parent(idx)
            if self.data[parent_idx] <= self.data[idx]:
                break
            self._swap(parent_idx, idx)
            idx = parent_idx

    def _shiftDown(self, idx):
        while self._left_child(idx) < self.size:
            j = self._left_child(idx)
            if j + 1 < self.size and self.data[j + 1] < self.data[j]:
                j += 1
            if self.data[idx] <= self.data[j]:
                break
            self._swap(idx, j)
            idx = j

    def _swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        min_heap = MinHeap(k)

        record =
