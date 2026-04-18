from math import log10, ceil

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))

    def reverse(self, n):
        number_length = floor(log10(n)) + 1
        rev: int = 0
        while n > 0:
            rev += 10 ** (number_length - 1) * (n % 10)
            number_length -=1
            n //=10
        return rev