#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_counts = Counter(moves)
        return move_counts['U'] == move_counts['D'] and move_counts['L'] == move_counts['R']
# @lc code=end

