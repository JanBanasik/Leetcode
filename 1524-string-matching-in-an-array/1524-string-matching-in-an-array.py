class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        temp = " ".join(words)
        result = [x for x in words if temp.count(x) > 1]
        return result