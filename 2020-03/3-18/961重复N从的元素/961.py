from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        """
        hash table的方法就不说了，很简单
        2N个元素，有N+1个不同的元素，其中一个重复了N次，所以剩余的N个都是不同的元素
        如果N个重复元素都分的很开，每个都隔一个不同的元素，必有三邻域出现重复数字
        所以思路就来了
        """
        for i in range(len(A) - 2):
            if A[i] == A[i + 1] or A[i] == A[i + 2]:
                return A[i]
        return A[-1]  # 有可能[2, 0, 面试题17.16化妆师, 2]


if __name__ == '__main__':
    test = Solution()
    print(test.repeatedNTimes([1, 6, 6, 9]))