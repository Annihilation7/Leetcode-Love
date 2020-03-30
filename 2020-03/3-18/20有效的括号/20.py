

class Solution:
    def isValid(self, s: str) -> bool:

        """典型的栈的应用"""
        stack = []
        record = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for elem in s:
            if elem in record:
                stack.append(elem)
            else:
                if len(stack) == 0 or record[stack[-1]] != elem:
                    return False
                stack.pop()

        return len(stack) == 0