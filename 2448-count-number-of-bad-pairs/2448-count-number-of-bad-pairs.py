class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        totalNumberOfPairs = (n - 1) * n // 2
        # good pair if:
        # nums[j] = (nums[i] - i) + j
        # for i < j
        # so: (nums[i] - i) = (nums[j] - j)
        counter = defaultdict(int)
        goodPairs = 0
        for index, value in enumerate(nums):
            counter[value - index] +=1
        
        for key, value in counter.items():
            goodPairs += (value) * (value - 1) // 2
            
        return totalNumberOfPairs - goodPairs