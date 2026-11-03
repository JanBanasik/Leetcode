class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        return sum(abs(x - m) for x in nums)