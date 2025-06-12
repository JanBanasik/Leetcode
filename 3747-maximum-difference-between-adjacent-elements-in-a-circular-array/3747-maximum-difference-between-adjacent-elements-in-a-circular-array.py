class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n: int = len(nums)
        res: int = 0
        for i in range(n - 1):
            res = max(res, abs(nums[i] - nums[i+1]))
        return max(res, abs(nums[n - 1] - nums[0]))