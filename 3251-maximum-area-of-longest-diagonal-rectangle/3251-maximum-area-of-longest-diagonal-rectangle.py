class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        currentMaxDiagSquared = -1
        currentMaxArea = -1
    
        for a, b in dimensions:
            diag = a ** 2 + b ** 2
            area = a * b
            if diag > currentMaxDiagSquared or (
                diag == currentMaxDiagSquared and area > currentMaxArea
            ):
                currentMaxDiagSquared, currentMaxArea = diag, area
            
        
        return currentMaxArea