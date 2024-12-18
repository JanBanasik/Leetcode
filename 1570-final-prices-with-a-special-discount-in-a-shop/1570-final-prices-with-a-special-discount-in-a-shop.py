class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            ans.append(prices[i])
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break
        return ans