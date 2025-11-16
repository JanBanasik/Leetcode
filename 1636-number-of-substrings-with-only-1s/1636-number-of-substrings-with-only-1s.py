def sum_of_next_integers(n):
    return (n + 1) * n // 2
class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        temp = 0
        result = 0
        for i in s:
            if i == "0" and temp:
                result += sum_of_next_integers(temp)
                temp = 0
            elif i == "1":
                temp +=1
        if temp:
            result += sum_of_next_integers(temp)
        return result % mod
            