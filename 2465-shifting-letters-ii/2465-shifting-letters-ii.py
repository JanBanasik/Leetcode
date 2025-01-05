class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        tab = [0] * n
        for left, right, shiftType in shifts:
            if shiftType == 1:
                tab[left] +=1
                if right + 1 < n:
                    tab[right + 1] -=1
            else:
                tab[left] -=1
                if right + 1 < n:
                    tab[right + 1] +=1

        numberOfShifts = 0
        result: str = ""
        for index, value in enumerate(s):
            numberOfShifts += tab[index]
            numberOfShifts %= 26
            if numberOfShifts < 0:
                numberOfShifts += 26
            
            shiftedChar = chr(
                (ord(s[index]) - ord("a") + numberOfShifts) % 26 + ord("a"))
            result += shiftedChar
        return result