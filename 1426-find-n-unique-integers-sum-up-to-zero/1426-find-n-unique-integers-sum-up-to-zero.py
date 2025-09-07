class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result.append(0)
            n -=1
        
        currentValue = 1

        for _ in range(n // 2):
            result.append(currentValue)
            result.append(-currentValue)
            currentValue +=1
        return result