#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 121
#  Author      : ZhenyuMa
#  Created     : 2020/3/31 9:11 下午
#  Description : 这道题可以转换成那个求两个数的差的最大值，且被减数在减数的前面！！这道题是我永远的痛！


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit
