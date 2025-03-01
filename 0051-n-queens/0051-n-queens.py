from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        result = []
        self.solveAfterPlacing(board, n, 0, set(), result)
        return result

    def solveAfterPlacing(self, board, n, row, incorrectPlacements, result):
        if row == n:
            result.append(["".join(r) for r in board])  # Store correct board copy
            return
        
        for col in range(n):  # Place only in the current row
            if (row, col) not in incorrectPlacements:
                board[row][col] = 'Q'
                temp = self.findAndSaveIncorrectPlacements(row, col, n, incorrectPlacements)
                self.solveAfterPlacing(board, n, row + 1, incorrectPlacements | temp, result)
                board[row][col] = '.'  # Backtrack

    def findAndSaveIncorrectPlacements(self, i, j, n, existing):
        incorrectPlacements = set(existing)  # Preserve existing invalid positions
        
        # Mark all positions in the same column
        for row in range(n):
            incorrectPlacements.add((row, j))
        
        # Mark diagonal (top-left to bottom-right)
        x, y = i, j
        while x >= 0 and y >= 0:
            incorrectPlacements.add((x, y))
            x -= 1
            y -= 1
        x, y = i, j
        while x < n and y < n:
            incorrectPlacements.add((x, y))
            x += 1
            y += 1

        # Mark diagonal (top-right to bottom-left)
        x, y = i, j
        while x >= 0 and y < n:
            incorrectPlacements.add((x, y))
            x -= 1
            y += 1
        x, y = i, j
        while x < n and y >= 0:
            incorrectPlacements.add((x, y))
            x += 1
            y -= 1
        
        return incorrectPlacements
