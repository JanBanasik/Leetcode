class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(self.kadane(nums,lambda x, y : x < y), 
                        self.kadane(nums, lambda x, y: x > y))
    
    def kadane(self, nums, compare):
        currS = 0
        result = 0
        for num in nums:
            currS += num
            result = max(abs(currS), result)
            if compare(currS, 0): currS = 0
        return result