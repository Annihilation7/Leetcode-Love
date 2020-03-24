

from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        """用集合暴力循环一遍，超时！"""

        # count = 0
        # record = set()
        #
        # for elem in A:
        #     while elem in record:
        #         elem += 面试题17.16化妆师
        #         count += 面试题17.16化妆师
        #     record.add(elem)
        #
        # return count


        # """排序，O(nlogn)"""
        # A.sort()
        # count = 0
        #
        # for i in range(面试题17.16化妆师, len(A)):
        #     if A[i - 面试题17.16化妆师] >= A[i]:  # 注意在更新的时候会导致前面的数比后面的数大
        #         cur_count = A[i - 面试题17.16化妆师] - A[i]
        #         A[i] += cur_count + 面试题17.16化妆师
        #         count += cur_count + 面试题17.16化妆师
        #
        # return count


        """计数排序，O(n) 空间复杂度O(n)"""
        record = [0] * 40000
        max_num = -float('inf')  # 天花板
        count = 0

        for elem in A:
            record[elem] += 1
            max_num = max(max_num, elem)

        if max_num != -float('inf'):
            for i in range(max_num):
                if record[i] > 1:
                    cur_count = record[i] - 1  # 需要增加的个数
                    record[i + 1] += cur_count  # 增加到下一个数字上，其实就是累加
                    count += cur_count

            # 单独处理一下max
            if record[max_num] > 1:
                cur_count = record[max_num] - 1
                count += (1 + cur_count) * cur_count // 2

        return count
