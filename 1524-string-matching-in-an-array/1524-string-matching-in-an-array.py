class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result: list[str] = []
        for index, value in enumerate(words):
            for index2, value2 in enumerate(words):
                if index != index2 and value in value2:
                    result.append(value)
                    break
        return result