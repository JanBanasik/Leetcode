class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [str(1)]
        for _ in range(n - 1):
            dp.append(self.getRLE(dp[-1]))
        return dp[-1]

    def getRLE(self, number: str) -> str:
        counter: int = 1
        res = str()
        n: int = len(number)

        for i in range(1, n):
            if number[i] != number[i - 1]:
                res += (str(counter) + number[i - 1])
                counter = 0
            counter +=1
        res += (str(counter) + number[-1])
        return res
