import bisect
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        sieve = self.sieve(max(nums))
        first = self.find_first_less_than_target(sieve, nums[0])
        nums[0] -= sieve[first] if first is not None else 0
        for i in range(1, len(nums)):
            for prime in sieve[::-1]:
                if nums[i] - prime > nums[i - 1]:
                    nums[i] -= prime
                    break
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return False
        return True
    def sieve(self, n):
        tab = [True for _ in range(0, n + 1)]
        tab[0] = False
        tab[1] = False
        for i in range(2, n + 1):
            if tab[i]:
                for j in range(i * i, n + 1, i):
                    tab[j] = False
        return [x for x in range(0, n + 1) if tab[x]]
    
    
    def findPrime(self, sieve, index, nums):
        ix = self.find_first_less_than_target(sieve, nums[index])
        if ix is None:
            return ix
        while ix > 0 and nums[index] - sieve[ix] < nums[index - 1]:
            ix -=1
        return ix
    def find_first_less_than_target(self, sorted_list, target):
        index = bisect.bisect_left(sorted_list, target)
        if index == 0:
            return None
        return index - 1
