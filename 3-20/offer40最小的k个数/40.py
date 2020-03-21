

from typing import List
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """partition"""
        if k == 0 or k > len(arr):
            return []

        target = k - 1
        l = 0
        r = len(arr) - 1

        while True:
            idx = self.partition(arr, l, r)
            if idx == target:
                return arr[:idx + 1]
            elif idx < target:
                l = idx + 1
            else:
                r = idx - 1

    def partition(self, arr, l, r):
        """单路partition"""
        random_idx = random.randint(l, r)
        arr[random_idx], arr[l] = arr[l], arr[random_idx]
        v = arr[l]

        lt = l
        for i in range(l + 1, r + 1):
            if arr[i] < v:
                lt += 1
                arr[i], arr[lt] = arr[lt], arr[i]
        arr[l], arr[lt] = arr[lt], arr[l]
        return lt


if __name__ == "__main__":
    test = Solution()
    print(test.helper([0,1,2,3,4,5,6,7,8], 0, 8,3))
