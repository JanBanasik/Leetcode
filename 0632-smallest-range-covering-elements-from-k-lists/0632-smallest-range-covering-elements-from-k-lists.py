class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                merged.append((nums[i][j], i))
        merged.sort(key = lambda x: x[0])
        contains = [0 for _ in range(len(nums))]
        l = 0
        rangeStart, rangeEnd = 0, float('inf')
        counter = 0
        for r in range(len(merged)):
            contains[merged[r][1]] += 1
            if contains[merged[r][1]] == 1:
                counter +=1
            while counter == len(nums):
                if merged[r][0] - merged[l][0] < rangeEnd - rangeStart:
                    rangeStart, rangeEnd = merged[l][0], merged[r][0]
                contains[merged[l][1]] -= 1
                if contains[merged[l][1]] == 0:
                    counter -=1
                l +=1
        return [rangeStart, rangeEnd]