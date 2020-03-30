


from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        self.res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    self.get_num_up(board, i, j)
                    self.get_num_down(board, i, j)
                    self.get_num_left(board, i, j)
                    self.get_num_right(board, i, j)
                    return self.res

    def get_num_up(self, board, i, j):
        while i - 1 >= 0:
            if board[i - 1][j] == '.':
                i -= 1
            elif board[i - 1][j] == 'p':
                self.res += 1
                break
            else:
                break

    def get_num_down(self, board, i, j):
        while i + 1 < len(board):
            if board[i + 1][j] == '.':
                i += 1
            elif board[i + 1][j] == 'p':
                self.res += 1
                break
            else:
                break

    def get_num_left(self, board, i, j):
        while j - 1 >= 0:
            if board[i][j - 1] == '.':
                j -= 1
            elif board[i][j - 1] == 'p':
                self.res += 1
                break
            else:
                break

    def get_num_right(self, board, i, j):
        while j + 1 < len(board[0]):
            if board[i][j + 1] == '.':
                j += 1
            elif board[i][j + 1] == 'p':
                self.res += 1
                break
            else:
                break
