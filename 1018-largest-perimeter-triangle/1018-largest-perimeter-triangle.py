class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n: int = len(nums)

        for i in range(n - 2):
            j = i + 1; k = i + 2
            if self.triangleCondition(nums[i], nums[j], nums[k]):
                return nums[i] + nums[j] + nums[k]
        return 0
    
    def triangleCondition(self, a, b, c):
        return (a + b > c) and (b + c > a) and (a + c > b)
