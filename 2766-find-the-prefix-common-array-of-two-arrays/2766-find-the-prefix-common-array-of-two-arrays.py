class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        result = [0] * len(A)
        for index, (valueA, valueB) in enumerate(zip(A, B)):
            result[index] = result[index - 1]
            if valueA == valueB:
                result[index] +=1
            else:
                if valueA in setB:
                    result[index] +=1
                if valueB in setA:
                    result[index] +=1
                setA.add(valueA)
                setB.add(valueB)
            
        return result