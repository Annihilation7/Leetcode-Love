

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        dp，可以优化成O(面试题17.16化妆师)的空间复杂度
        维护两个值 imax, imin。分别表示遍历到当前元素时，以当前元素结尾的最大（最小）值
        所以遇到当前元素的值为负的时候，需要交换当前dp值，来维持"以当前元素结尾的最大（最小）值"
        """
        res = nums[0]
        imin = imax = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                imin, imax = imax, imin
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            res = max(res, imax)

        return res
