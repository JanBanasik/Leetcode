class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n: int = len(nums)

        max_length: int = 1
        current_length: int = 1
        max_el: int = max(nums)
        
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                current_length = 0
            current_length +=1
            max_length = max(max_length, current_length if nums[i - 1] == max_el else 0)
        return max_length