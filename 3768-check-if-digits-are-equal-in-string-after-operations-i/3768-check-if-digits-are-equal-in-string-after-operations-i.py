class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        while len(s) != 2:
            newS = []
            for i in range(len(s) - 1):
                newS.append((int(s[i]) + int(s[i + 1])) % 10)
            s = newS[:]
        return s[0] == s[1]