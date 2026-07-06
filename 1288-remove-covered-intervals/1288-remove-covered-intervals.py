class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))

        result = []

        for interval in intervals:
            if not result: result.append(interval); continue

            last = result[-1]
            if not last[1] >= interval[1]:
                result.append(interval)
        return len(result)
