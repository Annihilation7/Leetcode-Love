


class Solution:
    def simplifyPath(self, path: str) -> str:

        tmp_str = path.split('/')
        stack = []

        for elem in tmp_str:
            if len(stack) and elem == '..':
                stack.pop()
            # 要算上 '' 以及 '..' 因为和上一个条件并不是互斥的条件
            elif elem != '' and elem != '.' and elem != '..':
                stack.append(elem)

        return '/' + '/'.join(stack)


if __name__ == '__main__':
    test = Solution()
    print(test.simplifyPath("/home/"))

