

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.res = []
        candidates.sort()  # 排序为了去重
        self.helper(candidates, 0, target, [])
        return self.res

    def helper(self, candidates, start_idx, target, cur_nums):
        if target == 0:
            self.res.append(cur_nums[:])
            return

        for i in range(start_idx, len(candidates)):
            if i > start_idx and candidates[i - 1] == candidates[i]:
                continue
            residual = target - candidates[i]
            if residual < 0:
                break
            # 标准回溯
            cur_nums.append(candidates[i])
            self.helper(candidates, i + 1, residual, cur_nums)
            cur_nums.pop()