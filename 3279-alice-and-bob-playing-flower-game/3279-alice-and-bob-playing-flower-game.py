class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        
        odd_n, even_n = self.calculateOddCount(n), self.calculateEvenCount(n)

        odd_m, even_m = self.calculateOddCount(m), self.calculateEvenCount(m)

        return odd_n * even_m + odd_m * even_n
        
    def calculateOddCount(self, upperBound):
        return (upperBound + 1) // 2 

    def calculateEvenCount(self, upperBound):
        return upperBound // 2