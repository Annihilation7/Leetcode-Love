

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        diff = []
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                diff.append(nums[i] - nums[i - 1])

        if len(diff) == 0:
            return 1  # 全是一样的元素且数量大于2

        dp = [2] * len(diff)
        for i in range(1, len(dp)):
            if diff[i - 1] * diff[i] < 0:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
