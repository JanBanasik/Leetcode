class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = defaultdict(int)
        for index, c in enumerate(s):
            h[c] = max(h[c], index)
        l = 0
        r = 0
        maxRightIndex = 0
        parts = []
        while r < len(s):
            maxRightIndex = max(maxRightIndex, h[s[r]])
            if maxRightIndex == r:
                parts.append(r - l + 1)
                l = r + 1
            r +=1
        return parts
