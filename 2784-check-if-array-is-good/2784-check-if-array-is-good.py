class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n: int = len(nums)
        numbers: set[int] = set(range(1, n))
        double_last: bool = False

        for num in nums:
            if num not in numbers and num == (n - 1):
                double_last = True
            numbers.discard(num)
            
        return not numbers and double_last