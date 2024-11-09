import math
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x
        res = bin(x)[2::]
        n -=1
        zerosNeeded = int(math.log(n, 2)) + 1
        diff = max(0, zerosNeeded - res.count("0"))  
        res = "0" * diff + res
        val = bin(n)[2::]
        x = len(val) - 1
        res = list(res)
        for i in range(len(res) - 1, -1, -1):
            if res[i] == "0":
                if val[x] == "1":
                    res[i] = "1"
                x -=1
                if x == -1:
                    break
        res = "".join(res)
        return int(res, 2)