class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res: int = 0
        for c in s:
            if c == '(':
                stack.append(1)
            elif c == ')':
                stack.pop()
            
            res = max(res, len(stack))
        return res