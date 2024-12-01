class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = set()
        for i in arr:
            if i in l:
                return True
            if i % 2 == 0:
                l.add(i // 2)
            l.add(i * 2)
        return False
            