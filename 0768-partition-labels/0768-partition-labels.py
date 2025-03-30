class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = defaultdict(list)
        for index, c in enumerate(s):
            h[c].append(index)
        l = 0
        r = 0
        maxRightIndex = 0
        parts = []
        while r < len(s):
            maxRightIndex = max(maxRightIndex, h[s[r]][-1])
            h[s[r]].pop(0)
            if maxRightIndex == r:
                parts.append(r - l + 1)
                l = r + 1
            r +=1
        return parts
