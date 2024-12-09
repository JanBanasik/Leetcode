class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                res.append(i - 1)
        res.append(len(nums) - 1)
        
        ans = []
        for a, b in queries:
            if bisect.bisect_left(res, a) != bisect.bisect_left(res, b):
                ans.append(False)
            else:
                ans.append(True)
        return ans