from math import factorial
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counters = defaultdict(int)
        result: int = 0
        for c in s:
            counters[c] +=1
        
        for key, value in counters.items():
            result += 1 if value >= 3 else 0
        
        lastPositions: dict[str, int] = dict()
        used = defaultdict(set)

        for index, value in enumerate(s):
            if value in lastPositions:
                for i in range(lastPositions[value] + 1, index):
                    if s[i] not in used[value]:
                        used[value].add(s[i])
                        result +=1
                
            lastPositions[value] = index
        
        return result
