

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        回溯+记忆化搜索
        aaaaaia   -----  [aaa, aa, aia, aaia]
        """
        self.recorder = {}
        return self.helper(s, wordDict)

    def helper(self, s, worddict):
        if not s:
            return True

        if self.recorder.get(s, False):
            return False  # 前面肯定是有过这个了

        for word in worddict:
            if len(s) >= len(word) and s[:len(word)] == word:
                if not self.helper(s[len(word):], worddict):
                    self.recorder[s[len(word):]] = True  # 记忆
                else:
                    return True

        return False

if __name__ == '__main__':
    test = Solution()
    print(test.wordBreak("cars", ["car","ca","rs"]))