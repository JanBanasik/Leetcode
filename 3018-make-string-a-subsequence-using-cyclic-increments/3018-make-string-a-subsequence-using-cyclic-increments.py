class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            val = (ord(str1[i]) + 1)
            if str1[i] == str2[j] or chr(val - 26 if val > 122 else val) == str2[j]:
                j +=1
            i +=1
        return j == len(str2)