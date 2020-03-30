


class Solution:
    def integerBreak(self, n: int) -> int:
        """1d dp"""
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])

        return dp[n]


if __name__ == '__main__':
    test = Solution()
    print(test.integerBreak(10))
