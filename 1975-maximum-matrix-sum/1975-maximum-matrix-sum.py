class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_count: int = 0
        min_abs_value: int = float('inf')
        total_sum: int = 0
        for row in matrix:
            for value in row:
                if value < 0:
                    negative_count += 1
                abs_value = abs(value)
                min_abs_value = min(min_abs_value, abs_value)
                total_sum += abs_value
        return total_sum - 2 * min_abs_value if negative_count % 2 else total_sum