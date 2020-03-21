

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """暂时先写个2d dp吧，1d的没写出来"""
        dp = [[0] * len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(dp)):
            for j in range(len(triangle[i])):
                l = max(j - 1, 0)
                r = min(j, len(triangle[i - 1]) - 1)
                dp[i][j] = min(dp[i - 1][l], dp[i - 1][r]) + triangle[i][j]

        return min(dp[-1])
