#  -*- coding: utf-8字符串转换整数 -*-

#  Editor      : Pycharm
#  File        : 46
#  Author      : ZhenyuMa
#  Created     : 2020/3/30 12:00 上午
#  Description : 回溯


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.visited = [False] * len(nums)
        self.helper(nums, [])
        return self.res

    def helper(self, nums, cur_res):
        if len(cur_res) == len(nums):
            self.res.append(cur_res[:])
            return

        for i in range(len(nums)):
            if not self.visited[i]:
                cur_res.append(nums[i])
                self.visited[i] = True
                self.helper(nums, cur_res)
                cur_res.pop()
                self.visited[i] = False


if __name__ == "__main__":
    test = Solution()
    print(test.permute([1, 2, 3]))


