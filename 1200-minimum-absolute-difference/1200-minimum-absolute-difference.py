class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n: int = len(arr)
        min_diff: int = min([arr[i] - arr[i - 1] for i in range(1, n)])
        result = []
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i-1], arr[i]])
        return result