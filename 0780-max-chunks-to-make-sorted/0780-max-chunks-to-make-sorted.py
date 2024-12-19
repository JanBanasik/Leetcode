class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        counter = 0
        maxEl = 0
        n = len(arr)
        for i in range(n):
            maxEl = max(maxEl, arr[i])
            if maxEl == i:
                counter +=1
        return counter