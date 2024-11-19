class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        lastOccurenceDict = {}
        tempSum = 0
        result = 0

        for right in range(len(nums)):
            l = lastOccurenceDict.get(nums[right], -1)

            while left <= l or right - left + 1 > k:
                tempSum -= nums[left]
                left +=1
            
            lastOccurenceDict[nums[right]] = right
            tempSum += nums[right]
            if right - left + 1 == k:
                result = max(result, tempSum)
        return result
