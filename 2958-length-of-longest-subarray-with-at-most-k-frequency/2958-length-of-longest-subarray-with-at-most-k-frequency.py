class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_l = 0
        hashmap = {}
        left = 0
        n = len(nums)
        for right in range(n):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
            if hashmap[nums[right]] > k:
                while nums[left] != nums[right]:
                    hashmap[nums[left]] -=1
                    left +=1
                hashmap[nums[left]] -=1
                left +=1
            max_l = max(max_l, right - left + 1)
        return max_l
            