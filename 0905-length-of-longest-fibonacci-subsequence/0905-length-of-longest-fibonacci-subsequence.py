class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashmap = {num: idx for idx, num in enumerate(arr)}
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        maxLength = 0

        for i in range(n):
            for j in range(i):
                prevEl = arr[i] - arr[j]
                if prevEl < arr[j] and hashmap.get(prevEl, n + 1) < j:
                    dp[i][j] = dp[j][hashmap[prevEl]] + 1
                else:
                    dp[i][j] = 2
                maxLength = max(maxLength, dp[i][j])
                
        return maxLength if maxLength > 2 else 0