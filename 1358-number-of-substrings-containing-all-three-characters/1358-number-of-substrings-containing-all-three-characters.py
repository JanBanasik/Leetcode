#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counters: List[int] = [0, 0, 0]
        
        left: int = 0
        result: int = 0
        for right in range(len(s)):
            counters[ord(s[right]) - ord('a')] += 1
            
            while all(counters):
                counters[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            result += left
        return result
# @lc code=end

