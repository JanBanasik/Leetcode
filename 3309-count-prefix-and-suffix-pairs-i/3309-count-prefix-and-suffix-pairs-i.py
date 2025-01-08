class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter: int = 0
        n: int = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    counter +=1
        return counter
    
    def isPrefixAndSuffix(self, string1: str, string2: str):
        return string2.startswith(string1) and string2.endswith(string1)