class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        n = len(nums)
        for i in range(1, n):
            prefix.append(max(prefix[-1], nums[i]))
        
        for i in range(n - 2, -1, -1):
            suffix.append(max(suffix[-1], nums[i]))
        suffix = suffix[::-1]

        res = 0
        for i in range(1, n - 1):
            res = max(res, (prefix[i - 1] - nums[i]) * suffix[i + 1])
        return res
        