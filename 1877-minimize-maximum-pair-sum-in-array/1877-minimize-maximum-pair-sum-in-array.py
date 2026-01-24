class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n: int = len(nums)
        result: int = -float('inf')
        for i in range(n // 2):
            result = max(result, nums[i] + nums[n - i - 1])
        return result