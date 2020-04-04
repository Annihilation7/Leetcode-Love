#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 33.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 9:46 下午
#  Description : 经典二分搜索


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1

        # 核心的关键：左中位数，收缩左边界！！非常的核心
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:  # [mid, r]有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:  # [l, mid]有序
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return -1 if nums[l] != target else l