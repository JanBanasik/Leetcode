class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        original = s[:]
        while True:
            s = s[1::] + s[0]
            if s == goal:
                return True
            if s == original:
                break
        return False