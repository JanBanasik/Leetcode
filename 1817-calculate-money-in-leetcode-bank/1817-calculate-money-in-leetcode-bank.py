class Solution:
    def totalMoney(self, n: int) -> int:
        mondayMoney = 0
        dollarsToPutToday: int = 0
        totalMoney: int = 0
        for i in range(1, n + 1):
            if i % 7 == 1: # indicating Monday
                mondayMoney +=1
                dollarsToPutToday = mondayMoney
            totalMoney += dollarsToPutToday
            dollarsToPutToday +=1
        return totalMoney