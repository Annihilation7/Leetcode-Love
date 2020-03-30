

from typing import List

class Solution:
    def massage(self, nums: List[int]) -> int:
        """小偷不偷村庄了，改行当化妆师了？和小偷问题是一模一样的！！！"""
        if len(nums) == 0:
            return 0

        dp = [0] * len(nums)

        for i in range(len(nums)):
            left_num = dp[i - 2] if i - 2 >= 0 else 0
            right_num = dp[i - 1] if i - 1 >= 0 else 0
            dp[i] = max(left_num + nums[i], right_num)

        return dp[-1]