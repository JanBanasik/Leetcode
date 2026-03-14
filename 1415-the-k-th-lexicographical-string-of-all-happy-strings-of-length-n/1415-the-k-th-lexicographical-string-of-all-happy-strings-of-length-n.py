#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings_count = 3 * 2  ** (n - 1)
        if k > happy_strings_count:
            return ""
        
        # main thing is that there will always be same number of those starting with a,b,c
        first_bucket = happy_strings_count // 3
        chars = ['a', 'b', 'c']
        result = ""
        first_char = chars[(k - 1) // first_bucket]
        result += first_char
        k = (k - 1) % first_bucket + 1     
        for _ in range(n - 1):
            options = [c for c in chars if c != result[-1]]
            first_bucket = first_bucket // 2
            if k <= first_bucket:
                result += options[0]
            else:
                result += options[1]
                k -= first_bucket
        return result

# @lc code=end

