class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        cumSum = nums[0]
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cumSum += nums[i]
            else:
                cumSum = nums[i]
            result = max(result, cumSum)
            
        return result    