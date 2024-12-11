class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            l = 0
            r = n - 1
            t = 0
            while l <= r:
                mid = (r - l) // 2 + l
                if nums[mid] - nums[i] <= 2 * k:
                    t = mid
                    l = mid + 1
                else:
                    r = mid - 1
            res = max(res, t - i + 1)
        return res
        