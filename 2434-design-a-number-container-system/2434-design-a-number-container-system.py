from collections import defaultdict
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.numberIndicesMap = defaultdict(SortedList)
        self.indexNumberMap = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if index in self.indexNumberMap:
            self.numberIndicesMap[self.indexNumberMap[index]].remove(index)
            self.indexNumberMap[index] = number
            self.numberIndicesMap[number].add(index)
        else:
            self.indexNumberMap[index] = number
            self.numberIndicesMap[number].add(index)

    def find(self, number: int) -> int:
        res = self.numberIndicesMap[number]
        if not res:
            return -1
        return res[0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)