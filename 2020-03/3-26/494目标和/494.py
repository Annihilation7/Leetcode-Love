

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """只能看懂记忆化搜索。。。"""
        self.res = 0
        self.record = {}
        return self.helper(0, nums, S, 0)

    def helper(self, idx, nums, S, cur_s):
        if idx == len(nums):
            return cur_s == S

        if (idx, cur_s) in self.record:
            return self.record[(idx, cur_s)]

        res = self.helper(idx + 1, nums, S, cur_s + nums[idx]) + self.helper(idx + 1, nums, S, cur_s - nums[idx])
        self.record[(idx, cur_s)] = res
        return res
