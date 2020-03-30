


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """经典背包问题"""
        dp = [0] * (target + 1)
        dp[0] = 1  # 空集和为0，即为1种方案！非常的关键
        for i in range(1, len(dp)):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]

    def baoli(self, nums, target):
        def helper(nums, target):
            if target < 0:
                return

            if target == 0:
                self.res1 += 1

            for i in range(len(nums)):
                helper(nums, target - nums[i])

        self.res1 = 0
        helper(nums, target)
        return self.res1