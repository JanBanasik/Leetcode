class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr_stones: int = 10
        while n >= 0:
            if n < curr_stones:
                return bool(curr_stones % 2)
            n -= curr_stones
            curr_stones -=1