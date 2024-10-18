class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        for value in nums:
            maxOR |= value

        n = len(nums)
        counter = 0

        for subset in range(1 << n):
            currOR = 0
            for i in range(n):
                if subset & (1 << i):
                    currOR |= nums[i]
            if currOR == maxOR:
                counter +=1
                
        return counter
