#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs_sorted: List[int] = self.counting_sort(costs)
        count: int = 0
        for cost in costs_sorted:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        return count

    def counting_sort(self, arr: List[int]) -> List[int]:
        max_value: int = max(arr)
        count: List[int] = [0] * (max_value + 1)
        for num in arr:
            count[num] += 1
        sorted_arr: List[int] = []
        for i in range(len(count)):
            sorted_arr.extend([i] * count[i])
        return sorted_arr
# @lc code=end

