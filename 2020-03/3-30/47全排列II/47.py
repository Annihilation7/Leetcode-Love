#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 47
#  Author      : ZhenyuMa
#  Created     : 2020/3/30 11:12 下午
#  Description : 回溯，和46相比仅仅多了一步去重而已


from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序便于去重
        self.visited = [False] * len(nums)
        self.res = []
        self.helper(nums, [])
        return self.res

    def helper(self, nums, cur_s):
        if len(cur_s) == len(nums):
            self.res.append(cur_s[:])
            return

        for i in range(len(nums)):
            # 去重的核心是前后两元素相同并且前面的没有被访问过，说明前面的元素已经完成回溯，当前元素就不需要再进行回溯了
            if self.visited[i] or (i > 0 and nums[i - 1] == nums[i] and not self.visited[i - 1]):
                continue
            cur_s.append(nums[i])
            self.visited[i] = True
            self.helper(nums, cur_s)
            cur_s.pop()
            self.visited[i] = False

