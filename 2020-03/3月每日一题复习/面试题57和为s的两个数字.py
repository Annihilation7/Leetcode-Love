#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 面试题57和为s的两个数字
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 3:13 下午
#  Description : hash或者双指针


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                return [nums[l], nums[r]]

        return []
