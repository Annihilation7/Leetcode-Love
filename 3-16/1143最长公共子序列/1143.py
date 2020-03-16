

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        """
        二维dp，dp[i][j]代表text1[:i+1]和text2[:j+1]最长的公共子序列，
        对于每一个新的索引i、j，需要看当前两字符串索引上的字符是否相等，若相等：
        dp[i][j] = dp[i-1][j-1] + 1，若不相等，dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        最终返回dp[-1][-1]就是所求的text1和text2的最长公共子序列
        """

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]