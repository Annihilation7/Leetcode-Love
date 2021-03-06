#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 1.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/18 12:23 上午
#  Description : 简单hash table的题


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            if target - nums[i] in record:
                return [record[target - nums[i]], i]
            record[nums[i]] = i