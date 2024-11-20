class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        h = {'a':0, 'b':0, 'c':0}
        for val in s:
            h[val] +=1
        if any([x < k for x in list(h.values())]):
            return -1
        
        l = 0
        currC = {'a':0, 'b':0, 'c':0}
        maxL = 0
        for r in range(n):
            currC[s[r]] +=1
            if self.isValid(h, currC, k):
                maxL = max(maxL, r - l + 1)
            else:
                currC[s[l]] -=1
                l +=1
        return n - maxL

    def isValid(self, h, currC, k):
        for key, value in h.items():
            if value - currC[key] < k:
                return False
        return True
