class Solution:
    def solveNQueens(self, n):

        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):

            # All queens are placed
            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Try every column in this row
            for col in range(n):

                # Is this position attacked?
                if col in cols or \
                   (row - col) in diag1 or \
                   (row + col) in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Go to next row
                backtrack(row + 1)

                # Undo / Backtrack
                board[row][col] = "."

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return result