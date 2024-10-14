import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        score: int = 0

        for _ in range(k):
            score -= heapq.heappushpop(nums, math.floor(nums[0] / 3))
        
        return score