

class Solution:
    def longestPalindrome(self, s: str) -> int:
        record = {}
        res = 0
        for elem in s:
            record[elem] = record.get(elem, 0) + 1
            if record[elem] % 2 == 0:
                res += 2
        return res if res == len(s) else res + 1