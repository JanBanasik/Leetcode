class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result: int = 0
        for num in nums:
            curr = num
            temp = 0
            while curr in nums_set:
                temp +=1
                curr *= curr
            result = max(result, temp)
        return result if result > 1 else -1