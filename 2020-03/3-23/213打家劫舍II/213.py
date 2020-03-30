

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        原问题分解成两个子问题，因为第一个和最后一个是不能同时偷的
        所以偷第一个产生一组结果，偷最后一个产生一组结果，取最大值即可！
        取两个dp的最大值
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        dp = [0] * len(nums)

        for i in range(len(dp)):
            left_num = 0 if i - 2 < 0 else dp[i - 2]
            right_num = dp[i - 1] if i - 1 >= 0 else 0
            dp[i] = max(left_num + nums[i], right_num)

        return dp[-1]
