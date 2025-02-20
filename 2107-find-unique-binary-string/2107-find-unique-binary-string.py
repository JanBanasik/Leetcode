class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = [""]
        n = len(nums)
        nums = set(nums)
        self.generate(nums, n, ans, "")
        return ans[0]

    def generate(self, nums, n, ans, curr):
        if ans[0]:
            return
        if len(curr) == n:
            if curr not in nums:
                ans[0] = curr[:]
        else:
            self.generate(nums, n, ans, curr + "0")
            self.generate(nums, n, ans, curr + "1")