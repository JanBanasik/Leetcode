import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        score: int = 0

        for _ in range(k):
            currVal = -heapq.heappop(nums)
            score += currVal
            currVal = math.ceil(currVal / 3)
            heapq.heappush(nums, -currVal)
        
        return score