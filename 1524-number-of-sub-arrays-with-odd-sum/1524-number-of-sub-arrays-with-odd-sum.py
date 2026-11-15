class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        odd = 0; even = 0
        cumSum = 0
        for num in arr:
            cumSum = (cumSum + num) % 2
            if cumSum == 1:
                odd +=1
            else:
                even +=1
        return (odd * even + odd) % mod
        