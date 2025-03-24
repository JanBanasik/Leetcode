class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        merged = []
        
        for meeting in meetings:
            if not merged or merged[-1][-1] < meeting[0]:
                merged.append(meeting)
            else:
                merged[-1][-1] = max(merged[-1][-1], meeting[1])

        result: int = 0
        currLeft = 0
        
        for meeting in merged:
            result += max(0, meeting[0] - currLeft - 1)
            currLeft = meeting[1]
        result += max(0, days - merged[-1][1])
        return result
