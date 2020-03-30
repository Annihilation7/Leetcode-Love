

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp，维持增益
        """
        _sum = 0  # 全局唯一
        res = -float('inf')

        for i in range(len(nums)):
            if _sum < 0:
                _sum = nums[i] # 已经让和小于0了，增益失败，直接从当前数字开始计算和
            else:
                _sum += nums[i]  # 非负数，一定有增益，累加
            res = max(res, _sum)

        return res
