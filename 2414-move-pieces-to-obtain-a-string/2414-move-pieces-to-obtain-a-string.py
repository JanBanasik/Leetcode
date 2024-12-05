class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start = list(start)
        target = list(target)
        n = len(start)
        p = 0
        while p < n and target[p] == '_':
            p +=1

        for i in range(n):
            if start[i] != '_':
                if p >= n or (start[i] != target[p]) or (start[i] == 'L' and i < p) or (start[i] == 'R' and i > p):
                    return False
                p +=1
            while p < n and target[p] == '_':
                p +=1
        return p == n
        