from collections import defaultdict
from typing import List
from itertools import product
from functools import lru_cache


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.possible = defaultdict(list)
        for a in allowed:
            self.possible[a[:2]].append(a[2])

        return self._can_build(bottom)

    @lru_cache(None)
    def _can_build(self, layer: str) -> bool:
        if len(layer) == 1:
            return True

        keys = [layer[i : i + 2] for i in range(len(layer) - 1)]
        for key in keys:
            if key not in self.possible:
                return False
        # Generate all possible combinations for the next layer
        all_combinations = product(*(self.possible[key] for key in keys))

        return any(
            self._can_build("".join(combination)) for combination in all_combinations
        )
