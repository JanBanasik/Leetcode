class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if [x for x in start if x != '_'] != [x for x in target if x != '_']:
            return False
        start = list(start)
        target = list(target)
        n = len(start)
        p = 0
        while p < n and target[p] == '_':
            p +=1

        for i in range(n):
            if start[i] != '_':
                if start[i] != target[p]:
                    return False
                if start[i] == 'L' and i < p:
                    return False
                if start[i] == 'R' and i > p:
                    return False
                p +=1
            while p < n and target[p] == '_':
                p +=1
        return True
        