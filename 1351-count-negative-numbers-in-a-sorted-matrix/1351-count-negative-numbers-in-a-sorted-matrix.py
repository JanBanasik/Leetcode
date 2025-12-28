class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([sum([x < 0 for x in row]) for row in grid])