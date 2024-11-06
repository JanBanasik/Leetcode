class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        nums = [[x, bin(x).count("1")] for x in nums]

        for i in range(1, len(nums)):
            key = nums[i]
            ix = i - 1
            while ix >= 0 and nums[ix][0] > key[0]: # we should switch
                if nums[ix][1] != nums[ix + 1][1]:
                    return False
                nums[ix + 1] = nums[ix][:]
                ix -=1
        return True
        # hashmap - number : set_bits
        # just do insertion sort