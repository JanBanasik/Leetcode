class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        return max(self.check_subarray(nums, lambda x, y: x > y), self.check_subarray(nums, lambda x, y: x < y))
        
    def check_subarray(self, nums, predicate):
        max_length: int = 1
        curr_length: int = 1

        for i in range(1, len(nums)):
            if predicate(nums[i], nums[i - 1]):
                curr_length +=1
            else:
                curr_length = 1
            
            max_length = max(max_length, curr_length)

        return max_length