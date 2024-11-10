class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        minLength = float('inf')
        left = 0
        bit_counts= [0] * 32

        for right in range(len(nums)):
            self.updateBits(bit_counts, nums[right], 1)
            while left <= right and self.convertBitsToNum(bit_counts) >= k:
                minLength = min(minLength, right - left + 1)
                self.updateBits(bit_counts, nums[left], -1)
                left +=1
        return -1 if minLength == float('inf') else minLength
    def updateBits(self, bit_counts, num, delta):
        for pos in range(32):
            if num & (1 << pos):
                bit_counts[pos] += delta
    
    def convertBitsToNum(self, bit_counts):
        res = 0
        for pos in range(32):
            if bit_counts[pos]:
                res |= 1 << pos
        return res

