#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 42
#  Author      : ZhenyuMa
#  Created     : 2020/4/2 9:39 下午
#  Description : 暴力 & 动态规划


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        暴力，遍历每个槽，看它左边最高的柱子以及右边最高的柱子，是否这两个柱子的最小值
        要比当前槽的高度要高，如果高，才能接到该槽所盛放的雨水，盛放量为：
        min(max_left_height, max_right_heigh) - cur_height
        时间复杂度：O(N^2)
        本题的关键就是 左max_height以及右max_height
        """
        res = 0

        for i in range(len(height)):
            max_left_height, max_right_height = 0, 0
            for j in range(i):
                if height[j] > height[i]:
                    max_left_height = max(max_left_height, height[j])
            for k in range(i + 1, len(height)):
                if height[k] > height[i]:
                    max_right_height = max(max_right_height, height[k])
            if min(max_left_height, max_right_height) > height[i]:
                res += min(max_left_height, max_right_height) - height[i]

        return res

    def trap_dp(self, height: List[int]) -> int:
        """
        上面在计算左边最高和右边最高的时候有重复计算，因此可以用dp来解决。
        多了两个数组，一个left_max，其索引i代表i左侧（包括i）最大的柱子高度
        一个right_max，其所以i代表i右侧（包括i）最大柱子的高度
        但是此时的空间复杂度为:O(n)
        """
        if len(height) == 0:
            return 0

        left_max = [0] * len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(len(height)):
            offset = min(left_max[i], right_max[i]) - height[i]
            res += offset if offset > 0 else 0

        return res

    def trap_final(self, height: List[int]) -> int:
        """双指针优化，能够将空间复杂度变成O(1)，需要理解一下。。。"""
        if len(height) == 0:
            return 0

        max_left_height = height[0]
        max_right_height = height[-1]
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            max_left_height = max(max_left_height, height[l])
            max_right_height = max(max_right_height, height[r])
            if max_left_height < max_right_height:
                res += max_left_height - height[l]
                l += 1
            else:
                res += max_left_height - height[r]
                r -= 1

        return res

if __name__ == "__main__":
    test = Solution()
    print(test.trap_dp([2, 0, 2]))