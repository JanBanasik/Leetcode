class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        s = set(range(n))
        for a, b in edges:
            s.discard(b)
        if len(s) > 1:
            return -1
        return list(s)[0]