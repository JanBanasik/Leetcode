class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n: int = len(nums)
        return sum(num**2 for index, num in enumerate(nums, 1) if n % index == 0)