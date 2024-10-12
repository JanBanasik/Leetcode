import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        groups:int = 0
        pq = []
        #print(intervals)
        for start, end in intervals:
            #print(start,end)
            if pq and pq[0] < start:
                heapq.heappop(pq)
            heapq.heappush(pq, end )
            #print(pq)
        return len(pq)
