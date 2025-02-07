class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        distinctBalls = 0
        indexColorMap = defaultdict(int)
        colorsCounts = defaultdict(int)
        res = []
        colors = set()
        for index, color in queries:
            if index in indexColorMap and indexColorMap[index] != color:
                colorsCounts[indexColorMap[index]] -=1
                colorsCounts[color] +=1
                if colorsCounts[indexColorMap[index]] == 0:
                    colors.discard(indexColorMap[index])
                
                indexColorMap[index] = color
                colors.add(color)
            elif index not in indexColorMap:
                indexColorMap[index] = color
                colorsCounts[color] +=1
                colors.add(color)
            
            res.append(len(colors))
        return res