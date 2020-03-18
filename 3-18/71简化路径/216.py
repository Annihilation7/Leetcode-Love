

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.helper(1, [], n, k)
        return self.res

    def helper(self, start_idx, cur_nums, n, k):
        if n == 0 and k == 0:
            self.res.append(cur_nums[:])
            return

        for i in range(start_idx, 10):
            residual = n - i
            if residual < 0:
                return

            cur_nums.append(i)
            k -= 1
            self.helper(i + 1, cur_nums, residual, k)
            cur_nums.pop()
            k += 1