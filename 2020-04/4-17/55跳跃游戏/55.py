#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 55.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/17 11:46 下午
#  Description : 遍历 看最大长度会不会比遍历的索引小


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0

        for i in range(len(nums)):
            if i > max_step:
                return False
            max_step = max(max_step, i + nums[i])

        return True