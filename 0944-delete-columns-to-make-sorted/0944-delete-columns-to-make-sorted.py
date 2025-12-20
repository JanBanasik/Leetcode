class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, columns = len(strs), len(strs[0])
        counter: int = 0
        
        for col in range(columns):
            for row in range(rows - 1):
                if strs[row][col] > strs[row + 1][col]:
                    counter +=1
                    break
        return counter