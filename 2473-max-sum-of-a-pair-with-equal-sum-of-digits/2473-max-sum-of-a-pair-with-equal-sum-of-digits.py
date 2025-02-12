
class Node:
    def __init__(self):
        self.first = -1 # the highiest 
        self.second = -1 # second highiest
    def append(self, value) -> None:
        newOrder = sorted([self.first, self.second, value])[-2:]
        self.second, self.first = newOrder
        
    def calculateResult(self):
        return (self.first + self.second if self.second != -1 else -1)
    
    def __repr__(self):
        return f"({self.first}, {self.second})"
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        h = defaultdict(Node)

        for num in nums:           
            sumOfDigits = self.getSumOfDigits(num)
            h[sumOfDigits].append(num)
 
        return max([v.calculateResult() for k, v in h.items()])

    def getSumOfDigits(self, number):
        result: int = 0
        
        while number > 0:
            result += number % 10
            number //= 10
        return result