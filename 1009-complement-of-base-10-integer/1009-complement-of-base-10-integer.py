from math import log

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        length: int = int(log(n, 2)) + 1
        return n ^ self.get_value(length)

    def get_value(self, length: int):
        return 2 ** length - 1