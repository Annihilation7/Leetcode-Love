#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 88
#  Author      : ZhenyuMa
#  Created     : 2020/3/31 9:05 下午
#  Description : 类似merge，只不过是从后往前进行的


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j = m - 1
        k = n - 1

        while i >= 0:
            if j < 0:
                nums1[i] = nums2[k]
                k -= 1
            elif k < 0:
                nums1[i] = nums1[j]
                j -= 1
            elif nums1[j] >= nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
            i -= 1