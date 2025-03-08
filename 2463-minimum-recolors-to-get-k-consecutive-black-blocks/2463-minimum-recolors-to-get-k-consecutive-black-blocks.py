class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        whiteCount = 0
        minBlocks = float('inf')
        for r in range(0, len(blocks)):
            whiteCount += 1 if blocks[r] == "W" else 0
            if r - l + 1 == k:
                minBlocks = min(minBlocks, whiteCount)
                whiteCount -= 1 if blocks[l] == "W" else 0
                l +=1
        print(l, r)
        return minBlocks
        