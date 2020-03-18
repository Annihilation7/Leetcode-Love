

from typing import List
from collections import deque


class MaxDeque:
    def __init__(self):
        """单调队列的实现"""
        self.data = deque()

    def enqueue(self, val):
        """往里仍元素的时候要保证val前的元素都比它大"""
        while len(self.data) and self.data[-1] < val:
            self.data.pop()
        self.data.append(val)

    def dequeue(self, val):
        """必须要和val相等才能pop，否则维持原样"""
        if len(self.data) and self.data[0] == val:
            self.data.popleft()

    @property
    def max(self):
        return self.data[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        self.aux_data = MaxDeque()

        for i in range(len(nums)):
            if i < k - 1:
                self.aux_data.enqueue(nums[i])
            else:
                self.aux_data.enqueue(nums[i])
                res.append(self.aux_data.max)
                self.aux_data.dequeue(nums[i - k + 1])

        return res

