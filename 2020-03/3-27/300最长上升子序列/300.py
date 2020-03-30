

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """O(nlogn) dp"""
        cache = []

        for i in range(len(nums)):
            if len(cache) == 0 or nums[i] > cache[-1]:
                cache.append(nums[i])
                continue

            l = 0
            r = len(cache) - 1
            while l < r:
                mid = l + (r - l) // 2
                if cache[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid
            cache[l] = nums[i]

        return len(cache)
