from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)

        for row, seat in reservedSeats:
            reserved[row].add(seat)

        families = 2 * n

        for seats in reserved.values():
            left = not seats.intersection({2, 3, 4, 5})
            middle = not seats.intersection({4, 5, 6, 7})
            right = not seats.intersection({6, 7, 8, 9})

            if left and right:
                continue
            elif left or middle or right:
                families -= 1
            else:
                families -= 2

        return families