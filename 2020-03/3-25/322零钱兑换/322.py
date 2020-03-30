
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """标准简单dp"""
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 初始化，0元钱没办法凑

        # 遍历每个amount
        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1