class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n: int = len(nums)
        numbers: set[int] = set(range(1, n))
        double_last: bool = False

        for num in nums:
            numbers.discard(num)
            
        
        return not numbers and nums.count(n - 1) == 2