class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        for i in range(len(s)):
            ix = ord(s[i]) - ord("a")
            first[ix] = i if first[ix] == -1 else first[ix]
            last[ix] = i
        
        result: int = 0
        for i in range(26):
            if first[i] == -1 or first[i] == last[i]:
                continue
            result += len(set(s[first[i]+1:last[i]]))
        return result