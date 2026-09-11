class Solution:
    def exist(self, board, word):

        def search(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False

            if board[r][c] != word[i]:
                return False

            ch = board[r][c]
            board[r][c] = "#"

            if (search(r+1, c, i+1) or
                search(r-1, c, i+1) or
                search(r, c+1, i+1) or
                search(r, c-1, i+1)):
                return True

            board[r][c] = ch
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if search(r, c, 0):
                    return True

        return False