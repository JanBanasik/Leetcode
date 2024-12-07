class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            maxSizeBag = (right - left) // 2 + left
            if self.isPossible(maxSizeBag, nums, maxOperations):
                right = maxSizeBag
            else:
                left = maxSizeBag + 1
        return left
    
    def isPossible(self, maxSizeBag, nums, maxOperations):
        total = 0
        for num in nums:
            operations = math.ceil(num/maxSizeBag) - 1
            total += operations
            if total > maxOperations:
                return False
        return True
