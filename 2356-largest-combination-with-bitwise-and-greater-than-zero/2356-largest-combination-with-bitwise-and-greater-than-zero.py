class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        m = 0
        for i in candidates:
            m = max(m, len(bin(i)[2::]))
        candidates = [[x, self.fillBinary(x, m)] for x in candidates]
        ans = [0 for _ in range(m)]

        for candidate in candidates:
            value, binaryForm = candidate
            for i in range(len(binaryForm)):
                if binaryForm[i] == "1":
                    ans[i] +=1
        return max(ans)
    
    def fillBinary(self, x, m):
        value = bin(x)[2::]
        return "0" * (m - len(value)) + value