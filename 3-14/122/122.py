

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        贪心算法
        前后两天的利润"：profit = pricrs[i] - prices[i - 1]
        连续上涨日：p0p1p2p3p4...pn profit = pn - p0 这个结果和第一天买第二天卖。。
            n-1个重复后的结果是一样的。
        明天的price比当前的price小，那么就保持。

        所以贪心算法的策略就是第二天比第一天price高，我们就买，否则就保持就完事了。
        """
        profit = 0
        for i in range(1, len(prices)):
            differ = prices[i] - prices[i - 1]
            if differ > 0:
                profit += differ
        return profit

    def maxProfit_dfs(self, prices: List[int]) -> int:
        """暴力搜索，超时，但是回溯的思想很好，一定要懂"""

        def helper(prices, idx, profit, status):
            """
            :param prices: 原数组
            :param idx: 进行交易到第几天了
            :param profit: 当前利润
            :param status: 1表示当前持有股票，所以可以保持不动或者卖出。
                        0表示当前不持有股票，所以可以保持或者买入
            """
            if idx == len(prices):
                self.res = max(self.res, profit)
                return

            # 保持
            helper(prices, idx + 1, profit, status)

            if status == 0:  # 尝试买入
                helper(prices, idx + 1, profit - prices[idx], 1)
            else:  # 尝试卖出
                helper(prices, idx + 1, profit + prices[idx], 0)

        self.res = 0
        helper(prices, 0, 0, 0)
        return self.res


if __name__ == '__main__':
    test = Solution()
    test_case = [7, 1, 5, 3, 6, 4]
    print(test.maxProfit_dfs(test_case))



