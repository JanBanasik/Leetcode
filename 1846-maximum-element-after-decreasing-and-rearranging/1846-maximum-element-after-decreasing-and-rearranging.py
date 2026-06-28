#
# @lc app=leetcode id=1846 lang=python3
#
# [1846] Maximum Element After Decreasing and Rearranging
#

# @lc code=start
from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # best case we have answer equal to the length of the array
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]
# @lc code=end

