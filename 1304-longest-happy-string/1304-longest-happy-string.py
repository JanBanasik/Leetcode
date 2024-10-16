class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        l: list[int] = [[a, 'a'], [b, 'b'], [c, 'c']]
        l.sort()
        result: str = str()
        while True:
            #print(l, result)
            if l[2][0] <= 0:
                break
            if not result or result[-1] != l[2][1]:
                result += l[2][1] * min(2, l[2][0])
                l[2][0] -=2
            elif result[-1] == l[2][1]:
                result += l[2][1]
                l[2][0] -=1            
            if l[1][0] == 0:
                break
            result += l[1][1]
            l[1][0] -=1
            l.sort()
        return result