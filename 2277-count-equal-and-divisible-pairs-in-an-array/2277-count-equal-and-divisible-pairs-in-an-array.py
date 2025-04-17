class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        counter: int = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and (nums[i] == nums[j]):
                    counter +=1
        return counter