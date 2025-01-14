class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cumulativeSetA = set()
        cumulativeSetB = set()
        result = []
        for valueA, valueB in zip(A, B):
            cumulativeSetA.add(valueA)
            cumulativeSetB.add(valueB)
            result.append(len(cumulativeSetA & cumulativeSetB))
            
        return result