class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        result = ""
        n = len(word)
        while i < n:
            temp = ""
            for j in range(i, min(n, i + 9)):
                if not temp or temp[-1] == word[j]:
                    temp += word[j]
                if temp[-1] != word[j]:
                    break
            i += len(temp)
            
            result += str(len(temp)) + temp[0]
        return result
            