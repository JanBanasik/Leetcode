import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        counter = 0
        for i in range(len(nums) - 1):
            num = nums[i]
            lowerBound = lower - num
            upperBound = upper - num
            counter += (bisect_right(nums, upperBound, i + 1) - bisect_left(nums, lowerBound, i + 1))
        return counter
