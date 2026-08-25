class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        max_val: int = max(nums)
        num: int = k
        while num <= max_val:
            if num not in nums:
                return num
            num += k 
        return num