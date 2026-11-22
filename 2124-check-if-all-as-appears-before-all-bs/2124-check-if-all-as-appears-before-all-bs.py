from itertools import pairwise

class Solution:
    def checkString(self, s: str) -> bool:

        for x, y in pairwise(s):
            if x == 'b' and y == 'a':
                return False
        return True        