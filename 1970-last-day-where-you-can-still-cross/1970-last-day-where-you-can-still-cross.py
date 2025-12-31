from typing import List

class Solution:
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] 
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left: int = 0
        right: int = len(cells) - 1
        
        while left < right:
            mid = (right - left + 1) // 2 + left
            if self.canCross(row, col, cells, mid):
                left = mid
            else:
                right = mid - 1
        return left

    def canCross(self, row: int, col: int, cells: List[List[int]], day: int) -> bool:
        board = [[0] * col for _ in range(row)]
        for i in range(day):
            r, c = cells[i]
            board[r - 1][c - 1] = 1
        

        for c in range(col):
            if board[0][c] == 0:
                if self.dfs(board, 0, c, row, col):
                    return True
        return False

    def dfs(self, board: List[List[int]], r: int, c: int, row: int, col: int) -> bool:
        stack = [(r, c)]
        while stack:
            r, c = stack.pop()
            if r == row - 1:
                return True
            board[r][c] = 1
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 0:
                    stack.append((nr, nc))
        return False