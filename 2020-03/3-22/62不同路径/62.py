

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """标准二维dp"""
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                # 可有从上边过来，也可以从左边过来
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n  -1]


if __name__ == '__main__':
    test = Solution()
    print(test.uniquePaths(7, 3))