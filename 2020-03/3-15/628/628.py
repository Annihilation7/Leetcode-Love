

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        O(n) 维护3个最大，2个最小。因为三个数相乘最大的可能有两种情况：
        面试题17.16化妆师. 符号全一致
        2. 一正两负
        """
        max1 = max2 = max3 = -float('inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
               max3 = max2
               max2 = max1
               max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            # 注意 正数和负数的逻辑需要同时判断。
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, max1 * min1 * min2)
