class Solution:
    def sumAndMultiply(self, n: int) -> int:
        return self.get_num(n)
    def get_num(self, n):
        mult: int = 1
        result: int = 0
        s: int = 0
        while n > 0:
            digit = n % 10
            s += digit
            if digit != 0:
                result += digit * mult
                mult *=10
            n = n // 10
        return result * s