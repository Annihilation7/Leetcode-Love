#  -*- coding:utf-8 -*-

#  Editor      : Pycharm
#  File        : 11.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/18 下午10:48
#  Description : 一道双指针的小题


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            area = self._get_area(height, l, r)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, area)

        return max_area

    def _get_area(self, height, l, r):
        return (r - l) * min(height[l], height[r])