class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result: int = 0
        l: int = 0
        n: int = len(fruits)
        h = defaultdict(int)
        for r in range(n):
            h[fruits[r]] +=1
            while len(h) > 2:
                h[fruits[l]] -=1
                if h[fruits[l]] == 0:
                    del h[fruits[l]]
                l +=1
            result = max(result, r - l + 1)
        return result