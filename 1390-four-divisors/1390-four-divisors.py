class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(self._sum_if_four_divisors(num) for num in nums)
    
    def _sum_if_four_divisors(self, n: int) -> int:
        counter: int = 0
        sum_divisors: int = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                counter += 2 if i * i != n else 1
                sum_divisors += i + (n // i if i * i != n else 0)
            if counter > 4:
                return 0
        return sum_divisors if counter == 4 else 0
        