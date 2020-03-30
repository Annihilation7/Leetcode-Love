

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """记忆化搜索"""
        self.record = [-1] * len(nums)
        return self.helper(nums, 0)

    def helper(self, nums, start_idx):
        if start_idx >= len(nums):
            return 0

        if self.record[start_idx] != -1:
            return self.record[start_idx]

        res = 0
        for i in range(start_idx, len(nums)):
            res = max(res, self.helper(nums, i + 2) + nums[i])
        self.record[start_idx] = res

        return res

    def rob1(self, nums):
        """动态规划"""
        if len(nums) == 0:
            return 0

        dp = [0] * len(nums)

        for i in range(len(dp)):
            left_num = dp[i - 2] if i - 2 >= 0 else 0
            right_num = dp[i - 1] if i - 1 >= 0 else 0
            dp[i] = max(left_num + nums[i], right_num)
        return dp[-1]