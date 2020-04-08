#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 4.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/9 12:06 上午
#  Description : 惨痛的回忆


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.findKthElm(nums1, nums2, length // 2) + self.findKthElm(nums1, nums2, length // 2 + 1)) / 2
        else:
            return self.findKthElm(nums1, nums2, length // 2)

    def findKthElm(self, nums1, nums2, k):
        assert len(nums1) >= 1 and len(nums2) >= 1
        m, n = len(nums1), len(nums2)
        l = max(0, k)
        r = min(m, k - n)

        while l < r:
            mid = l + (r - l) // 2
            if nums1[mid] < nums2[k - mid - 1]:
                l = mid + 1
            else:
                r = mid
        num1_left_max = nums1[l - 1] if l > 0 else -float('inf')
        num2_left_max = nums2[k - l - 1] if l != k else -float('inf')
        return max(num1_left_max, num2_left_max)


