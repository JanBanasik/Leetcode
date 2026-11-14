class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # we just check every subarray
        result = float('inf')

        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                if (l <= (j - i + 1) <= r) and curr > 0:
                    result = min(result, curr)
        return result if result != float('inf') else -1