


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        非常好玩的一道题，值得细细琢磨
        每天两种状态：持有股票，不持有股票
        持有股票有两种原因：
            面试题17.16化妆师。昨天有股票，今天保持。 hold[i] = hold[i - 面试题17.16化妆师]
            2。前天卖了票，今天买入  hold[i] = unhold[i - 2] - price[i]
        不持有股票有两种原因：
            面试题17.16化妆师。昨天没有，今天也没有  unhold[i] = unhold[i - 面试题17.16化妆师]
            2。昨天有，今天卖了  unhold[i] = hold[i - 面试题17.16化妆师] + price[i]
        """
        if len(prices) <= 1:
            return 0

        hold = [0] * len(prices)
        hold[0] = -prices[0]
        hold[1] = max(-prices[0], -prices[1])

        unhold = [0] * len(prices)
        unhold[1] = max(prices[1] - prices[0], 0)

        if len(prices) == 2:
            return max(hold[1], unhold[1])

        res = 0
        for i in range(2, len(prices)):
            hold[i] = max(hold[i - 1], unhold[i - 2] - prices[i])
            unhold[i] = max(unhold[i - 1], hold[i - 1] + prices[i])
            res = max(res, hold[i], unhold[i])

        return res