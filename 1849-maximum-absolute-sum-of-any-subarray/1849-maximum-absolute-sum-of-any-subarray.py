class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(self.kadane1(nums), self.kadane2(nums))


    def kadane1(self, nums):
        currS = 0
        result = 0
        for num in nums:
            currS += num
            result = max(currS, result)
            if currS < 0: currS = 0
        return result
    
    def kadane2(self, nums):
        currS = 0
        result = float('inf')
        for num in nums:
            currS += num
            result = min(currS, result)
            if currS > 0: currS = 0
        return abs(result)