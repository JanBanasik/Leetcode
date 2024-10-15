class Solution:
    def minimumSteps(self, s: str) -> int:
        # problem is the same as move zeros
        # just backwards
        counter: int = 0
        s = list(s)
        temp: int = 0
        left = len(s) - 1
        for right in range(len(s) - 1, -1, -1):
            if s[right] == "0":
                temp +=1
            else:
                counter += temp
        return counter
