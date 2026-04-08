from typing import List
from functools import reduce
from operator import xor
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        result: int = 0
        mod: int = 10**9 + 7
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % mod
        return reduce(xor, nums, result)