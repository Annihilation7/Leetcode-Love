

class Solution:
    def numDecodings(self, s: str) -> int:
        """记忆化搜索"""
        self.record = {}
        return self.helper(s)

    def helper(self, s):
        # 解码失败
        if s in self.record:
            return self.record[s]

        if len(s) > 0 and s[0] == '0':
            return 0
        # 递归终止的条件
        if len(s) <= 1:
            return 1

        one_solution = self.helper(s[1:])
        two_solution = 0
        if len(s) >= 2 and int(s[:2]) <= 26:
            two_solution = self.helper(s[2:])

        # 记忆
        self.record[s] = one_solution + two_solution
        return one_solution + two_solution


if __name__ == '__main__':
    test = Solution()
    print(test.numDecodings('12120'))