#
# @lc app=leetcode id=2126 lang=python3
#
# [2126] Destroying Asteroids
#

# @lc code=start
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
        return True
# @lc code=end

