from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache
        def dp(i):
            if i < 0:
                return 0
            
            return max(dp(i - 1), dp(i - 2) + nums[i])
        
        return dp(len(nums) - 1)