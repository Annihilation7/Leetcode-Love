

class Solution:
    def climbStairs(self, n: int) -> int:
        """记忆化搜索"""
        # return self.helper1(n)
        self.memo = [0] * (n + 1)
        self.helper(n)
        return self.memo[n]

    def helper(self, n):
        if n <= 2:
            return n

        if self.memo[n] == 0:
            self.memo[n] = self.helper(n - 1) + self.helper(n - 2)
        return self.memo[n]

    def helper1(self, n):
        """动态规划"""
        if n == 1:
            return 1
        if n == 2:
            return 2

        i = 1
        j = 2
        _sum = None
        for _ in range(2, n):
            _sum = i + j
            i = j
            j = _sum
        return _sum


if __name__ == '__main__':
    test = Solution()
    print(test.climbStairs(10))
