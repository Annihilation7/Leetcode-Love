#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 1049.py
#  Author      : ZhenyuMa
#  Created     : 2020-04-07 22:40
#  Description : 居然能转换成背包问题


from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 求背包容量，sum//2
        total_storage = sum(stones)
        storage = total_storage // 2

        package = [0] * (storage + 1)

        for i in range(len(stones)):
            for j in range(storage, -1, -1):
                if j < stones[i]:
                    break
                package[j] = max(package[j], package[j - stones[i]] + stones[i])

        return total_storage - 2 * package[-1]
