class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        for i in range(n - 2):
            if nums[i] == 0:
                for k in range(0, 3):
                    nums[i + k] = not nums[i + k]
                op +=1
        for i in range(n - 1, n - 4, -1):
            if not nums[i]:
                return -1
        return op
        