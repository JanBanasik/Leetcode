from sortedcontainers import SortedList
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        s = SortedList(gifts)
        for _ in range(k):
            s.add(math.floor(s.pop(-1)**(0.5)))
        return sum(s)