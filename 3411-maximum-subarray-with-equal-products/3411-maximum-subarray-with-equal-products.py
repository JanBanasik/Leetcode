from math import gcd, lcm


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        # prod / (gcd * lcm) is non-decreasing as the subarray grows, so once
        # the product overshoots gcd * lcm it can never come back. Undershoot
        # (single element > 1) can still turn into equality by extending.
        result: int = 0
        n = len(nums)

        for i in range(n):
            product, g, l = 1, 0, 1

            for j in range(i, n):
                x = nums[j]
                product *= x
                g = gcd(g, x)   
                l = lcm(l, x)

                if product > g * l:
                    break

                if product == g * l:
                    result = max(result, j - i + 1)

        return result