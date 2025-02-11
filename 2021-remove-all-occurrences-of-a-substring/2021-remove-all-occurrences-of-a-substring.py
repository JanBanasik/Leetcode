class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        partLength = len(part)
        i = 0
        while i < len(s) - partLength + 1:
            print(s[i:i+partLength])
            if s[i:i+partLength] == part:
                newString = s[0:i] + s[i+partLength:]
                s = newString[:]
                i = i - partLength
            
            i +=1
        return s


            
            
            