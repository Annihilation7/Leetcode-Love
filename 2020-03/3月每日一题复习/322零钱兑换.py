#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 322零钱兑换.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/6 12:09 下午
#  Description : 一道背包问题


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0amount肯定是没有满足条件的coins的

        for i in range(1, len(dp)):  # i代表当前的amount
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == "__main__":
    test = Solution()
    print(test.coinChange([1], 2))