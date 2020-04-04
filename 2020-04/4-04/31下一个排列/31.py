#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 31.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 9:04 下午
#  Description : 很巧妙的方法


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        # step1 找到相邻的升序
        i = len(nums) - 2
        j = len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        # step2: 当前相邻升序并不一定是要交换的，要找到i的后继
        if i >= 0:
            for k in range(len(nums) - 1, i, -1):
                if nums[k] > nums[i]:
                    nums[k], nums[i] = nums[i], nums[k]
                    break

        # step3 i后升序排列，目前i后肯定是降序排列
        k = i + 1
        l = len(nums) - 1
        while k < l:
            nums[k], nums[l] = nums[l], nums[k]
            k += 1
            l -= 1


if __name__ == "__main__":
    test = Solution()
    print(test.nextPermutation([1, 2, 3]))