class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negCount = 0
        n = len(nums)
        for index, val in enumerate(nums):
            if val > 0:
                posCount = n - index
                return max(posCount, negCount)
            elif val < 0:
                negCount +=1
        return negCount