class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        n = len(nums)
        marked = set()
        score = 0
        for index, value in enumerate(nums):
            heapq.heappush(heap, (value, index))
        while heap:
            value, index = heapq.heappop(heap)
            if index not in marked:
                score += value
                for k in range(-1, 2):
                    marked.add(index + k)
        return score