class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [[x.count('0'), x.count('1')] for x in strs]

        @cache
        def dp(ix,m,n):
            if m < 0 or n < 0:
                return -float('inf')
            if ix == len(counters):
                return 0
            return max(dp(ix + 1, m ,n), dp(ix + 1, m - counters[ix][0], n - counters[ix][1]) + 1)
        return dp(0,m,n)