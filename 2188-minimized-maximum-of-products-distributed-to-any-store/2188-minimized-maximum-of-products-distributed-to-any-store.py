class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)
        while l < r:
            mid = (r - l) // 2 + l
            if self.canDistribute(n, mid, quantities):
                r = mid
            else:
                l = mid + 1
        return l
    
    def canDistribute(self, n, mid, quantities):
        c = 0
        for quantity in quantities:
            c += math.ceil(quantity / mid)
        return c <= n
