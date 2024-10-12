class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[nums[i]] = i