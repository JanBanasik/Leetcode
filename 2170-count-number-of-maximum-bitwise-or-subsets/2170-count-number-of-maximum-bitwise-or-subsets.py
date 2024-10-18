class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        for value in nums:
            maxOR |= value
        
        counter = [0]
        self.backtrack(0, maxOR, nums, 0, counter)

        return counter[0]

    def backtrack(self, currOR, maxOR, nums, index, counter):
        if index == len(nums):
            return
        copyOR = currOR
        currOR |= nums[index]
        if currOR == maxOR:
            counter[0] +=1

        self.backtrack(copyOR, maxOR, nums, index + 1, counter)
        self.backtrack(currOR, maxOR, nums, index + 1, counter)