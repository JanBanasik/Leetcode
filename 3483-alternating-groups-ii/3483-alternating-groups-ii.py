class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        
        n = len(colors)
        res = 0
        left = 0
        right = 1
        while right < n:
            if colors[right] == colors[right - 1]:
                left = right
                right +=1
                continue
            right +=1
            if right - left < k:
                continue
            res +=1
            left +=1
        return res