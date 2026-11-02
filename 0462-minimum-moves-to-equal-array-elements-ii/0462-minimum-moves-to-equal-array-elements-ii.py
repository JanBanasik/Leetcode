import math
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        median: int = math.ceil(self.get_median(nums))

        return sum(abs(x-median) for x in nums)
    
    def get_median(self, nums: list[int]) -> float:
        nums.sort()
        n: int = len(nums)
        if n % 2 == 1:
            return nums[n // 2]
        return (nums[n // 2 - 1] + nums[n // 2]) / 2