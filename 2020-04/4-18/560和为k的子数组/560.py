#  -*- coding:utf-8 -*-

#  Editor      : Pycharm
#  File        : 560.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/18 下午11:16
#  Description : 由于是连续区间，从某一个位置开始一段数字的和与target相等，
#                所以类似积分图的思想，建立record, 从头开始记录_sum，然后找_sum-target是否
#                在record中，不在就添加进record，在的话就是找到了，即加上前面_sum-target
#                出现的次数就可以了


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        record = {}
        record[0] = 1

        _sum = 0
        res = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if (_sum - k) in record:
                res += record[_sum - k]
            record[_sum] = record.get(_sum, 0) + 1

        return res




