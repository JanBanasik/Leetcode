class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = float('inf')
        prefSumHeap = []
        temp = 0
        for i, num in enumerate(nums):
            temp += num
        
            if temp >= k:
                res = min(res, i + 1)
            
            while (prefSumHeap and temp - prefSumHeap[0][0] >= k):
                res = min(res, i - heappop(prefSumHeap)[1])
            
            heappush(prefSumHeap, (temp, i))
        return (-1 if res == float('inf') else res)