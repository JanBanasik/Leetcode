class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        c = 0
        s = 0
        currNum = 1
        for currNum in range(1, n + 1):
            if currNum not in banned:
                s += currNum
                if s > maxSum:
                    return c
                c +=1
        return c