class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        hashmap = {}
        res = []
        for i in range(len(matrix[0])):
            temp = []
            if matrix[0][i] == 1:
                temp.append(1)
            else:
                temp.append(0)
            for j in range(1,len(matrix)):
                if matrix[j][i] == 1:
                    temp.append(temp[-1] + 1)
                else:
                    temp.append(0)
            res.append(temp)

        result = []
        for i in range(len(res[0])):
            temp = []
            for j in range(len(res)):
                temp.append(res[j][i])
            result.append(temp)
        result = [sorted(x) for x in result]
        
        area = 0
        for i in range(len(result)):
            for j in range(len(result[i])):
                height = result[i][j]
                width = len(result[i]) - j
                area = max(area,height * width)
        return area