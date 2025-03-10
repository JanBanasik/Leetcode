class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
    
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)
        
    def _atLeastK(self, word, k):
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vowelCounts = {}
        l = 0
        consonantsCount = 0
        res = 0
        for r in range(len(word)):
            letter = word[r]

            if letter in vowels:
                vowelCounts[letter] = vowelCounts.get(letter, 0) + 1
            else:
                consonantsCount +=1
            
            while len(vowelCounts) == 5 and consonantsCount >= k:
                res += len(word) - r
                start_letter = word[l]
                if start_letter in vowels:
                    vowelCounts[start_letter] = vowelCounts.get(start_letter, 0) - 1
                    if vowelCounts[start_letter] == 0:
                        vowelCounts.pop(start_letter)
                else:
                    consonantsCount -=1
                l +=1
        return res    
                    