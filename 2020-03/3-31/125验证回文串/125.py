#  -*- coding: utf-8 -*-

#  Editor      : Pycharm
#  File        : 125
#  Author      : ZhenyuMa
#  Created     : 2020/3/31 9:22 下午
#  Description : 典型的双指针法


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r:
                if s[l].upper() == s[r].upper():
                    l += 1
                    r -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome("A man, a plan, a canal: Panama"))