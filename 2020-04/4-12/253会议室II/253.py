#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 253.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/12 3:17 下午
#  Description : 转化为同一时间进行的最大会议数量的问题，并且题解也非常的巧妙，一定要记住


from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        total_intervals = sorted(
            [(elem[0], 1) for elem in intervals] + [(elem[1], -1) for elem in intervals],
            key=lambda x: (x[0], x[1])  # x[1]而不是-x[1] 因为要先结束，再开始
        )
        res = 0
        cur_res = 0

        for i in range(len(total_intervals)):
            cur_res += total_intervals[i][1]
            res = max(res, cur_res)

        return res


if __name__ == "__main__":
    test = Solution()
    print(test.minMeetingRooms([])
