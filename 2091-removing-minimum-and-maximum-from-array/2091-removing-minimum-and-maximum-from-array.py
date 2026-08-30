class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        lower = min(min_index, max_index)
        upper = max(min_index, max_index)

        n = len(nums)

        return min(
            upper + 1,                 # oba usuwasz od lewej
            n - lower,                 # oba usuwasz od prawej
            lower + 1 + (n - upper)    # jeden od lewej, drugi od prawej
        )