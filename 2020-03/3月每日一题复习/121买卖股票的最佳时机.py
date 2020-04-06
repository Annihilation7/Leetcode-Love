#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 121买卖股票的最佳时机.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/6 12:36 下午
#  Description : 一道小dp，和求后面与前面的最大差值的题的意思是一样的


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        dp = [0] * len(prices)
        min_price = prices[0]

        for i in range(1, len(dp)):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[-1]