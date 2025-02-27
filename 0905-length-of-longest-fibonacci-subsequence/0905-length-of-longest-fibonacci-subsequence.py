class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        dp = [[2] * n for _ in range(n)]

        maxLength = 0

        for i in range(2, n):

            left = 0
            right = i - 1

            while left < right:
                s = arr[left] + arr[right]

                if s > arr[i]:
                    right -=1
                elif s < arr[i]:
                    left +=1
                
                else:
                    dp[i][right] = dp[right][left] + 1
                    maxLength = max(maxLength, dp[i][right])
                    right -=1
                    left +=1
        
        
        return maxLength if maxLength > 2 else 0