class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        s = set()

        for num in nums:
            if num < k:
                return -1
            s.add(num)
        
        return len(s) - (1 if k in s else 0)