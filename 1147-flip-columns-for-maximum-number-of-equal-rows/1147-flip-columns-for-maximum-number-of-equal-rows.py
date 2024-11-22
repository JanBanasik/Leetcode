class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashmap = {}
        for row in matrix:
            pattern = self.findPattern(row)
            hashmap[pattern] = hashmap.get(pattern, 0) + 1
        return max(list(hashmap.values()))
    
    def findPattern(self, row):
        c = 1
        el = row[0]
        pattern = str()
        for i in range(1, len(row)):
            if row[i] != row[i - 1]:
                pattern += str(c) + "|"
                c = 1
                el = row[i]
            else:
                c +=1
        pattern += str(c)
        return pattern