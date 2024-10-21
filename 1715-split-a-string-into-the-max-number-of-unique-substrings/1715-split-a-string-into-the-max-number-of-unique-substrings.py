class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        self.n = len(s)
        self.backtrack(s, 0, set())
        return self.ans

    def backtrack(self, s, currentIndex, usedStrings):
        if currentIndex == self.n:
            self.ans = max(self.ans, len(usedStrings))
        
        for i in range(currentIndex, len(s)):
            temp = s[currentIndex:i + 1]
            if temp not in usedStrings:
                usedStrings.add(temp)
                self.backtrack(s, i + 1, usedStrings)
                usedStrings.remove(temp)

                