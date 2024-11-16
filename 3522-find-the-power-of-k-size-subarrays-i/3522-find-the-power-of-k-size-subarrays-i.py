class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            flag = True
            for j in range(1, k):
                if nums[i+j] != nums[i+j-1] + 1:
                    flag = False
                    break
            if not flag:
                ans.append(-1)
            else:
                ans.append(nums[i+k-1])
        return ans