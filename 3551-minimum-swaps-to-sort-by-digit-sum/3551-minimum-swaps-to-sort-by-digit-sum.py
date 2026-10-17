from functools import cache

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        new_arr = [
            (self.digit_sum(num), num, index)
            for index, num in enumerate(nums)
        ]
        new_arr.sort()

        visited = [False] * len(nums)
        result = 0

        for i in range(len(nums)):
            if visited[i] or new_arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = new_arr[j][2]
                cycle_size += 1

            result += cycle_size - 1

        return result

    @staticmethod
    @cache
    def digit_sum(num):
        return sum(int(d) for d in str(num))