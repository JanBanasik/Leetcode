class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        t = sentence.split(" ")
        for i in range(len(t) - 1):
            if t[i][-1] != t[i + 1][0]:
                return False
        return True