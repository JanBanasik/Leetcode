class Solution:
    def compressedString(self, word: str) -> str:
        temp: str = str()
        result: str = str()
        n: int = len(word)

        for index, char in enumerate(word):
            if not temp or temp[-1] == char:
                temp += char

            if temp[-1] != char or len(temp) == 9:
                result += str(len(temp)) + temp[0]
                if temp[-1] != char:
                    temp = char
                else:
                    temp = ""
                
        if temp:
            result += str(len(temp)) + temp[0]
        return result