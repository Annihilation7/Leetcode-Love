

from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        一道典型的回溯问题
        注意给定的字符串中会有重复元素，需要过滤。解决办法就是先排序，然后过滤
        """
        s = sorted(s)
        print(s)
        self.visited = [False] * len(s)
        self.res = []
        self.helper(s, 0, '')
        return self.res

    def helper(self, s, idx, cur_str):
        if idx == len(s):
            self.res.append(cur_str)
            return

        for i in range(len(s)):
            # 注意条件判断：首先访问过的元素不考虑，第二考虑重复元素，如果前一个元素
            # 已经被用过了，并且还和当前的元素相等，那么肯定是要产生重复项的
            # 所以直接continue就好
            if self.visited[i] or (i > 0 and s[i] == s[i - 1] and self.visited[i - 1]):
                continue
            self.visited[i] = True
            self.helper(s, idx + 1, cur_str + s[i])
            self.visited[i] = False


if __name__ == '__main__':
    test = Solution()
    print(test.permutation('abc'))