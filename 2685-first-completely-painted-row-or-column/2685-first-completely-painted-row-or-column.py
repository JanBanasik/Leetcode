from dataclasses import dataclass

@dataclass
class Point:
    row: int
    col: int
    
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        points = {}
        m = len(mat)
        n = len(mat[0])
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                points[mat[i][j]] = Point(i, j)
        
        for index, value in enumerate(arr):
            curr = points[value]
            row, col = curr.row, curr.col
            rows[row] +=1
            cols[col] +=1
            if rows[row] == n or cols[col] == m:
                return index