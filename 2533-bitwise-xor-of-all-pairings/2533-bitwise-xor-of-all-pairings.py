from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = self.swapArrays(nums1, nums2)
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        elif len(nums1) % 2 == 1:
            if len(nums2) % 2 == 1:
                return self.getArrayXor(nums1) ^ self.getArrayXor(nums2)
            else:
                return self.getArrayXor(nums2)

    def swapArrays(self, nums1, nums2):
        if len(nums2) % 2 == 1:
            return nums2, nums1
        return nums1, nums2
        
    def getArrayXor(self, numbers):
        return reduce(lambda a, b: a ^ b, numbers)
        