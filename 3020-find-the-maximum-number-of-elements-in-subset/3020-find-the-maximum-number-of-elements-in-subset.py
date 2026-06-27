from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 1

        # Special case: 1, because 1 ** 2 == 1
        ones = counter[1]
        if ones:
            result = max(result, ones if ones % 2 == 1 else ones - 1)

        for num in counter:
            if num == 1:
                continue

            if counter[num] >= 2:
                result = max(result, self._build_sequence(num, counter))

        return result

    def _build_sequence(self, start: int, counter: Counter[int]) -> int:
        length = 0
        current = start

        while counter[current] >= 2:
            length += 2
            current *= current

        # current is now the potential middle value
        if counter[current] == 1:
            return length + 1

        # No middle exists, so the last pair cannot be used
        return length - 1