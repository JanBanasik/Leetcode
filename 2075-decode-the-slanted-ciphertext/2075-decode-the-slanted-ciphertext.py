#
# @lc app=leetcode id=2075 lang=python3
#
# [2075] Decode the Slanted Ciphertext
#

# @lc code=start
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        parts: int = len(encodedText) // rows
        result: str = ""
        for i in range(parts):
            for j in range(i, len(encodedText), parts + 1):
                result += encodedText[j]
        return result.rstrip()
# @lc code=end

