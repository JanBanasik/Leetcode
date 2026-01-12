from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time: int = 0
        points = [Point(x, y) for x, y in points]
        for index, (left, right) in enumerate(zip(points, points[1:])):
            x_diff = abs(left.x - right.x)
            y_diff = abs(left.y - right.y)
            time += max(x_diff, y_diff)
        return time