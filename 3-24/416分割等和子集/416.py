

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)

        if _sum % 2 != 0:
            return False  # 不能被平分，一定是False

        bag_volume = _sum // 2  # 背包容量

        # 背包容量从0到bag_valume，初始化为-面试题17.16化妆师
        # self.record[i][j]如果等于1，表明用前i+1个元素能够填充容量为j的背包
        # self.redocr[i][j]如果等于0，表明用前i+1个元素不能填充容量为j的背包
        self.record = [[-1] * (bag_volume + 1) for _ in range(len(nums))]
        return self.helper(nums, bag_volume, len(nums) - 1)

    def helper(self, nums, c, idx):
        """
        考察索引为的元素，以及它前面的数字，能否填充容量为c的背包。
        :param nums: 原数组
        :param c: 背包容量
        :param start_idx: 考察的id
        :return: 能否被填充的结果——能(True)，不能(False)
        """
        if idx < 0:
            return False

        if c == 0:  # 条件满足
            return True

        if self.record[idx][c] != -1:
            return bool(self.record[idx][c])  # 直接返回记忆的结果

        # 这个元素我不要，我考察前面的元素能否填充这个背包
        res = self.helper(nums, c, idx - 1)
        if c >= nums[idx]:
            # 这个元素我要了，前提是你的背包容量要能容纳下这个元素，然后继续去考察前面的元素能否填充加了这个元素之后的背包
            # 两个条件满足一个就可以了，所以是或运算
            res = res or self.helper(nums, c - nums[idx], idx - 1)

        self.record[idx][c] = bool(res) # 记忆

        return res

    def helper_dp(self, nums):
        _sum = sum(nums)

        if _sum % 2 != 0:
            return False

        bag_volume = _sum // 2
        # dp[i]的意义——————用索引从 0到i这i+1个数字能否填充容量为i的背包
        dp = [-1] * (bag_volume + 1)  # 一维dp，通过滚动数组来优化

        # 边界条件，考察第一个元素作为dp数组的初始化
        for i in range(bag_volume + 1):
            dp[i] = (nums[0] == i)

        # 从第2个元素开始
        for i in range(1, len(nums)):
            for j in range(bag_volume, -1, -1):
                if j < nums[i]:
                    break  # 提前结束的一个优化
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[-1]  # 最后返回dp[-面试题17.16化妆师]，代表用这len(nums)个元素能否填充容量为bag_volume的背包。