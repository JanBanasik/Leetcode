class Solution:
    def countTriples(self, n: int) -> int:
        counter = 0
        for i in range(1, n):
            for j in range(i, n):
                var = (i ** 2 + j ** 2) ** 0.5
                if var > n:
                    break
                # print(i, j)
                counter += 2 * (var % 1 == 0)
        return counter