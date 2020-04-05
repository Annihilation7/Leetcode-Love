#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 34.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/5 10:45 下午
#  Description : 经典二分搜索


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 特判别
        if len(nums) == 0:
            return [-1, -1]

        # 先找左边，左中位数，收缩左边界
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        # 现在可以判断一下这个数是否存在
        if nums[l] != target:
            return [-1, -1]
        res_l = l

        # 找右边，右中位数，收缩右边界
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid

        return [res_l, r]