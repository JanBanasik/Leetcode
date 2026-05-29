
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([self.getSum(num) for num in nums])

    def getSum(self, num):
        result: int = 0
        while num > 0:
            result += num % 10
            num //=10
        return result