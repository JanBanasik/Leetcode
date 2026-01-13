from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        # first find lower and upper bounds for binary search
        lower = None
        upper = None
        for _, y, side in squares:
            if lower is None or y < lower:
                lower = y
            if upper is None or y + side > upper:
                upper = y + side
                
        while upper - lower > 1e-5:
            mid = (lower + upper) / 2
            lower_area = 0
            upper_area = 0
            for x, y, side in squares:
                if y >= mid:
                    upper_area += side * side
                elif y + side <= mid:
                    lower_area += side * side
                else:
                    lower_area += (mid - y) * side
                    upper_area += (y + side - mid) * side

            if lower_area < upper_area:
                lower = mid
            else:
                upper = mid
        return lower