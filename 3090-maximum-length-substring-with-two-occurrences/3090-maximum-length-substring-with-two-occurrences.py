class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter: list[int] = [0] * 26

        l: int = 0
        max_len: int = 0

        for r in range(len(s)):
            v = ord(s[r]) - 97
            counter[v] += 1

            while counter[v] > 2:
                counter[ord(s[l]) - 97] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len