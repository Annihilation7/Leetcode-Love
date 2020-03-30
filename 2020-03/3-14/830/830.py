

from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        """遍历，计数即可"""
        res = []
        i = 0

        while i < len(S):
            j = i + 1
            while j < len(S) and S[i] == S[j]:
                j += 1
            if j - i >= 3:
                res.append([i, j - 1])
            i = j

        return res
