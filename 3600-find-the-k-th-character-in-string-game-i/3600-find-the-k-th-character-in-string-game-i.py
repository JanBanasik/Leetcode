class Solution:
    def kthCharacter(self, k: int) -> str:
        aliceWord = "a"
        while len(aliceWord) < k:
            newToAdd = ""
            for i in range(len(aliceWord)):
                newToAdd += self.shift(aliceWord[i])
            aliceWord += newToAdd
        return aliceWord[k - 1]
    
    def shift(self, char: str):
        newCharValue = ord(char) + 1
        if newCharValue > 123:
            newCharValue -= 26
        return chr(newCharValue)