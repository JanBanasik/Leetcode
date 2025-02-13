from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = SortedList(nums)
        steps = 0
        while len(nums) >= 2 and s[0] < k:
            val1 = s.pop(0)
            val2 = s.pop(0)
            s.add(val1 * 2 + val2)
            steps +=1
        return steps