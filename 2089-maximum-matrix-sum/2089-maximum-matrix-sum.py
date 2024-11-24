from functools import reduce
import operator

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        c = 0
        minEl = float('inf')
        n = len(matrix)
        s = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    c +=1
                minEl = min(minEl, abs(matrix[i][j]))
                s += abs(matrix[i][j])
         
        return s - (2 * minEl if c % 2 == 1 else 0)
        
