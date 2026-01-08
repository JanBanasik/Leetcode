from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] means max dot product of nums1[0:i] and nums2[0:j]
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(product,
                               dp[i - 1][j - 1] + product,
                               dp[i - 1][j],
                               dp[i][j - 1])
        return int(dp[m][n])