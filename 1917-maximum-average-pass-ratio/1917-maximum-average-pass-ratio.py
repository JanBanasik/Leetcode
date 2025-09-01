import heapq
from statistics import fmean

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        heap = [(self.calculate_new_gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)


        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (self.calculate_new_gain(p, t), p, t))

        return fmean(p / t for _, p, t in heap)
    
    
    def calculate_new_gain(self, p: int, t: int):
        return -(((p + 1) / (t + 1)) - ((p / t)))