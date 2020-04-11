#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 887.py
#  Author      : ZhenyuMa
#  Created     : 2020/4/11 11:19 下午
#  Description : dp


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        """K鸡，N层"""
        self.memo = {}
        return self.dp(K, N)

    def dp(self, K, N):
        if K == 1:
            return N
        if N == 0:
            return 0

        if (K, N) in self.memo:
            return self.memo[(K, N)]

        l = 1
        r = N
        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            broken = self.dp(K - 1, mid - 1)  # 碎
            not_broken = self.dp(K, N - mid)  # 没碎
            if not_broken > broken:
                l = mid + 1
                res = min(res, not_broken + 1)
            else:
                r = mid
                res = min(res, broken + 1)
        self.memo[(K, N)] = res
        return res