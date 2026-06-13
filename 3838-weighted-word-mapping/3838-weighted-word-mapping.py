class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result: str = str()

        for word in words:
            weight: int = self.get_weight(word, weights)
            weight = weight % 26
            result += chr(122 - weight)
        return result

    def get_weight(self, word: str, weights: List[int]):
        result: int = 0
        for c in word:
            result += weights[ord(c) - 97]
        return result