

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        start_idx = 0
        res = ''

        for i in range(len(S)):
            if S[i] == '(':
                stack.append('(')
            else:
                stack.pop()

            if len(stack) == 0:
                res += S[start_idx + 1: i]  # 这里直接清除外层括号了
                start_idx = i + 1

        return res


if __name__ == '__main__':
    test = Solution()
    print(test.removeOuterParentheses('(()())(())'))