class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for _ in range(n - 1):
            s = s + "1" + self.invert(s)[::-1]
        return s[k - 1]
    
    def invert(self, s):
        newS = ""
        for i in s:
            newS += "1" if i == "0" else "0"
        return newS