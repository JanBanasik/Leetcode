class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x: x[0])
        counters = [0 for _ in range(n)]
        free_rooms = [i for i in range(n)]
        end_times = []
        heapq.heapify(free_rooms)
        heapq.heapify(end_times)

        for start, end in meetings:
            
            while end_times and end_times[0][0] <= start:
                _end, room = heapq.heappop(end_times)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(end_times, (end,room))
            else:
                time,room = heapq.heappop(end_times)
                heapq.heappush(end_times, (time + end - start, room))
            counters[room] +=1
        return counters.index(max(counters))
