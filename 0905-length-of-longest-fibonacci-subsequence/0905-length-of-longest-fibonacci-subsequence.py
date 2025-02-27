class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        maxLength = 0

        n = len(arr)

        for i in range(n):
            for j in range(i):
                a, b = arr[j], arr[i]
                currLength = 2
                while (a + b) in num_set:
                    currLength +=1
                    maxLength = max(maxLength, currLength)
                    a, b = b, (a + b)
        return maxLength