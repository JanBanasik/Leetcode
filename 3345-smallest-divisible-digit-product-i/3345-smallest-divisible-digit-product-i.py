class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i: int = 0

        while True:
            if self.get_number_product(n + i) % t == 0:
                return n + i
            i +=1
    
    def get_number_product(self, number: int) -> int:
        product: int = 1
        while number > 0:
            product *= (number % 10)
            number = number // 10
            
        return product