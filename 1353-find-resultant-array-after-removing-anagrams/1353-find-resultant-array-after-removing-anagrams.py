class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        if len(words) < 2:
            return words
        
        values = [sorted(list(x)) for x in words]
        i = 0
        res = [words[0]]
        for _ in range(len(words)):
            try:
                if values[i] != values[i + 1]:
                    res.append(words[i + 1])
                i +=1
            except IndexError:
                break
        return res