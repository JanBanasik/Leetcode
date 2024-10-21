class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.backtrack(s, 0, str(), set())
    
    def backtrack(self, s, currentIndex, currentSubstring, usedStrings):
        if currentIndex == len(s) and not currentSubstring:
            return len(usedStrings)
        elif currentIndex == len(s):
            return 0
        
        newUsed = usedStrings.copy()
        currentSubstring += s[currentIndex]
        newUsed.add(currentSubstring)

        return max(self.backtrack(s, currentIndex + 1, currentSubstring, usedStrings),
        self.backtrack(s, currentIndex + 1, str(), newUsed))