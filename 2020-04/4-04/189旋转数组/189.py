#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 189.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/5 12:18 上午
#  Description : 要求空间复杂度为O(1)，需要一点技巧


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # 先翻转整个数组
        self._reverse(nums, 0, len(nums) - 1)
        # 翻转前k个
        self._reverse(nums, 0, k - 1)
        # 翻转k后面的
        self._reverse(nums, k, len(nums) - 1)

    def _reverse(self, nums, l, r):
        i = l
        j = r
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    test = Solution()
    a = [i for i in range(7)]
    test.rotate(a, 3)
    print(a)

