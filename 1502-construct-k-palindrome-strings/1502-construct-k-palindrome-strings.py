class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        lettersDict = defaultdict(int)
        for c in s:
            lettersDict[c] +=1
        
        oddCount = 0
        for key, value in lettersDict.items():
            oddCount += value % 2
        return not oddCount > k