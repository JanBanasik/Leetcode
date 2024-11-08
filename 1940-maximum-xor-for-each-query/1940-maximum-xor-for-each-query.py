class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        s = 0
        for num in nums:
            s ^= num
        n = len(nums)
        answer = []
        for i in range(n):
            answer.append(s ^ (2 ** maximumBit - 1))
            s ^= nums.pop(-1)
        return answer