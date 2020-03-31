#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 912
#  Author      : ZhenyuMa
#  Created     : 2020/3/31 8:53 下午
#  Description : 一个快排


from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums

    def _quick_sort(self, nums, l, r):
        if l >= r:
            return

        random_idx = random.randint(l, r)
        nums[l], nums[random_idx] = nums[random_idx], nums[l]
        v = nums[l]

        lt = l
        gt = r + 1
        i = l + 1

        while i < gt:
            if nums[i] < v:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] > v:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1

        nums[l], nums[lt] = nums[lt], nums[l]
        self._quick_sort(nums, l, lt - 1)
        self._quick_sort(nums, gt, r)


if __name__ == "__main__":
    test = Solution()
    print(test.sortArray([5, 4, 3, 2, 1]))