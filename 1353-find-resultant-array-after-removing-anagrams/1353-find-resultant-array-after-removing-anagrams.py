from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words

        result = [words[0]]
        prev_sorted = sorted(words[0])

        for word in words[1:]:
            curr_sorted = sorted(word)
            if curr_sorted != prev_sorted:
                result.append(word)
            prev_sorted = curr_sorted

        return result
