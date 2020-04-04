#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 15.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/4 3:53 下午
#  Description :


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:  # 最小的数都大于0了，肯定没有加起来等于0的了
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1

        return res