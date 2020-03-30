

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        end = 0
        max_pos = 0
        count = 0

        for i in range(len(nums) - 1):
            max_pos = max(max_pos, i + nums[i])

            if i == end:
                # 第i+1次的踏板范围全部跑完，才会更新一次count
                end = max_pos
                count += 1

            # end到终点，提前结束
            if end == len(nums) - 1:
                break

        return count

