

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.record = set()
        return self.helper(s, wordDict)

    def helper(self, s, wordDict):
        if not s:
            return True

        if s in self.record:
            return False

        for word in wordDict:
            if len(s) >= len(word) and s[:len(word)] == word:
                res = self.helper(s[len(word):], wordDict)
                if res:
                    return True
                else:
                    self.record.add(s)
        return False