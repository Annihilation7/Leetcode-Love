



class Solution:
    def compressString(self, S: str) -> str:
        res = ''

        i = 0
        while i < len(S):
            j = i + 1
            while j < len(S) and S[j] == S[i]:
                j += 1

            res = res + S[i] + str(j - i)
            i = j

        return res if len(res) < len(S) else S
