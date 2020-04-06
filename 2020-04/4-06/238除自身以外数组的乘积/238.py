#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 238.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/6 11:46 上午
#  Description : 两个record数组，分别记录除自己以外左边、右边的乘积结果


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 记录左积
        left_array = [1] * len(nums)
        for i in range(1, len(nums)):
            left_array[i] = left_array[i - 1] * nums[i - 1]

        # 记录右积
        right_array = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_array[i] = right_array[i + 1] * nums[i + 1]

        res = []
        for i in range(len(nums)):
            res.append(left_array[i] * right_array[i])

        return res
