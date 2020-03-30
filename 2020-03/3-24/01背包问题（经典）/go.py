

from typing import List


class Solution:
    def max_value01(self, values: List[int], weights: List[int], c: int) -> int:
        """每个物品的价值在values中，每个物品的重量在weights中，所给的重量为c"""
        self.values = values
        self.weights = weights
        self.c = c
        self.record = [[-1] * (c + 1) for _ in range(len(values))]
        return self.helper(len(values) - 1, c)

    def helper(self, idx, cur_c):
        """
        记忆化搜索
        对于每个idx，有两种选择
        第一个是我不装它
        第二个是我装它，前提是要重量能够满足条件
        """
        if idx < 0:
            return 0
        if self.record[idx][cur_c] != -1:
            return self.record[idx][cur_c]

        res = self.helper(idx - 1, cur_c)  # 不装，考虑前一个
        if cur_c >= self.weights[idx]:  # 装
            res = max(
                self.helper(idx - 1, cur_c - self.weights[idx]) + self.values[idx],
                res
            )
        self.record[idx][cur_c] = res

        return res

    def max_value01_dp(self, values: List[int], weights: List[int], c: int) -> int:
        """
        动态规划
        dim0 代表物品数量
        dim1 代表最大重量
        """
        dp = [[0] * (c + 1) for _ in range(len(values))]

        # 边界
        # 物品1(idx=0)依次放入容量从1到c的容器中所能获取的最大值
        for i in range(len(dp[0])):
            dp[0][i] = values[0] if weights[0] <= i else 0

        # 从第二个物品(idx=面试题17.16化妆师)开始算起
        for i in range(1, len(dp)):
            for j in range(len(dp[1])):
                dp[i][j] = dp[i - 1][j]  # 不考虑第i个物品
                # 考虑第i个物品，但是第i个物品的重量不能超过当前的容量
                if j >= weights[i]:
                    dp[i][j] = max(dp[i][j], values[i] + dp[i - 1][j - weights[i]])

        return dp[-1][-1]


    def max_value01_dp_space(self, values: List[int], weights: List[int], c: int) -> int:
        """将空间复杂度优化到O（C）"""
        dp = [-1] * (c + 1)
        # 边界
        for i in range(len(dp)):
            dp[i] = values[0] if i >= weights[0] else 0

        for i in range(1, len(values)):
            for j in range(len(dp) - 1, -1, -1):
                if j < weights[i]:  # 而且有性能上的优化
                    break
                dp[j] = max(dp[j - 1], values[i] + dp[j - weights[i]])

        return dp[-1]


if __name__ == '__main__':
    test = Solution()

    weights = [1, 2, 3]
    values = [6, 10, 12]
    print(test.max_value01(values, weights, 5))
    print(test.max_value01_dp(values, weights, 5))
    print(test.max_value01_dp_space(values, weights, 5))
