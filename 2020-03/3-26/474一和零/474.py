


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]

        for i in range(1, len(dp)):
            nums = self.count_num(strs[i - 1])
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]  # 先赋值，因为后面的条件可能不满足，就是说这个包先用原先的包顶替
                    zero_num, one_num = nums
                    if j >= zero_num and k >= one_num:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zero_num][k - one_num] + 1)

        return dp[-1][-1][-1]

    def count_num(self, string):
        res = [0] * 2
        for elem in string:
            res[int(elem)] += 1
        return res


if __name__ == '__main__':
    test = Solution()
    test.findMaxForm(['1', '2', '3'], 6, 9)