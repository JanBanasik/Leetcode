from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Two 1-indexed Fenwick trees to support Range Add and Range Sum
        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)
        
        def _add(bit: List[int], idx: int, val: int):
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)
                
        def _query(bit: List[int], idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        def range_add(l: int, r: int, val: int):
            # Add 'val' to all indices in 1-indexed range [l, r]
            _add(bit1, l, val)
            _add(bit1, r + 1, -val)
            _add(bit2, l, val * (l - 1))
            _add(bit2, r + 1, -val * r)

        def prefix_sum(idx: int) -> int:
            return _query(bit1, idx) * idx - _query(bit2, idx)

        def range_sum(l: int, r: int) -> int:
            # Return sum of elements in 1-indexed range [l, r]
            return prefix_sum(r) - prefix_sum(l - 1)

        last_pos = {}
        total_ans = 0
        curr_squares_sum = 0  # Tracks sum of f(i, r)^2 for 0 <= i <= r
        
        for r, x in enumerate(nums):
            # Convert 0-indexed positions to 1-indexed for the Fenwick Tree
            l_idx = last_pos.get(x, -1) + 2  # (p + 1) + 1
            r_idx = r + 1                    # r + 1
            
            # 1. Query the sum of current distinct counts in range [p + 1, r]
            sum_f = range_sum(l_idx, r_idx)
            
            # 2. Update the sum of squares ending at r:
            # S_r = S_{r-1} + 2 * sum(f) + count_of_updated_elements
            count = r_idx - l_idx + 1
            curr_squares_sum = (curr_squares_sum + 2 * sum_f + count) % MOD
            
            # 3. Increment distinct counts in range [p + 1, r] by 1
            range_add(l_idx, r_idx, 1)
            
            # 4. Accumulate into the total result and record last seen position
            total_ans = (total_ans + curr_squares_sum) % MOD
            last_pos[x] = r
            
        return total_ans