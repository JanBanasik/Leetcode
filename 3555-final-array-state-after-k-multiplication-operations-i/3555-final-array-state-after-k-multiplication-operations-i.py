from sortedcontainers import SortedList
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        s1 = SortedList(key = lambda x:(x[1], x[0]))
        for index, num in enumerate(nums):
            s1.add((index, num))
        for _ in range(k):
            i, val = s1.pop(0)
            nums[i] *= multiplier
            s1.add((i, val * multiplier))
        return nums