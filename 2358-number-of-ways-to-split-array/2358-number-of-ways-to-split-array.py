class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        counter = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                counter +=1
        return counter