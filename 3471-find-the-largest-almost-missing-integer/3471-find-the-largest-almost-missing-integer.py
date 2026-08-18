from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        c = Counter(nums)

        candidates = nums if k == 1 else (nums[0], nums[-1])
        return max((x for x in candidates if c[x] == 1), default=-1)