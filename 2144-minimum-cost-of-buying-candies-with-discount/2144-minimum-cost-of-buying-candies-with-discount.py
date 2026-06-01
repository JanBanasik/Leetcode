class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)
        
        cost.sort(reverse=True)

        n: int = len(cost)
        result: int = 0
        for i in range(0, n, 3):
            result += cost[i] + self._safe_get(cost, i + 1)
        return result
    
    def _safe_get(self, cost, index, default=0):
        try:
            return cost[index]
        except IndexError:
            return default