class Solution:
    def findScore(self, nums: List[int]) -> int:
        tab = sorted([(val, index) for index, val in enumerate(nums)], key = lambda x: (x[0], x[1]))
        marked = set()
        n = len(tab)
        score = 0
        for i in range(0, n):
            value, index = tab[i]
            if index not in marked:
                score += value
                for k in range(-1, 2):
                    marked.add(index  + k)
        return score