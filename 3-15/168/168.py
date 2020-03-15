


class Solution:
    def convertToTitle(self, n: int) -> str:

        """
        10进制转26进制，但是起始不是从0开始的，所以余数是0的时候需要特殊处理，
        处理方式是左右两边同时减1
        """
        res = ''
        while n:
            c = n % 26
            n //= 26

            # 等于0的时候要特殊处理
            if c == 0:
                c = 26
                n -= 1

            res = chr(65 + c - 1) + res

        return res

if __name__ == '__main__':
    test = Solution()
    print(test.convertToTitle(701))
