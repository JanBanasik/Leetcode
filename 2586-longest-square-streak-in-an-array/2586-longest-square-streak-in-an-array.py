class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        hashmap = {}
        for num in nums:
            sq = num ** 0.5
            if sq in hashmap:
                hashmap[num] = hashmap[sq] + 1
            else:
                hashmap[num] = 1
        res = max(hashmap.values())
        return res if res != 1 else -1 