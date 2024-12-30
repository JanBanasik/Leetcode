class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0 for i in range(high + 1)]
        dp[0] = 1
        dp[zero] +=1
        dp[one] +=1
        for i in range(len(dp)):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
        return (sum(dp[low::]) // 2) % mod

