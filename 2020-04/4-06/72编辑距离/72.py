#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 72.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/6 11:18 上午
#  Description : 经典dp


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # 边界1
        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] + 1
        # 边界2
        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i - 1] + 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]