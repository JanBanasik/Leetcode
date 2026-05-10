#
# @lc app=leetcode id=2770 lang=python3
#
# [2770] Maximum Number of Jumps to Reach the Last Index
#

# @lc code=start
from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        dp: List[int] = [-1] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)    
        return dp[-1]
# @lc code=end

