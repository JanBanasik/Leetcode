class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)
        if n == 1:
            return matrix[0]
        if m == 1:
            temp = []
            for i in matrix:
                temp += [x for x in i]
            return temp
        f = len(matrix) * len(matrix[0])
        spiral = []
        i = 0
        j = 0
        check = 0
        h = 0
        while f > 0:
            
            f -=1
            print(i,j, f,check)
            spiral.append(matrix[i][j])
            print(spiral)
            if check == 0:
                j +=1
            elif check == 1:
                i +=1
            elif check == 2:
                j -=1
            elif check == 3:
                i -=1
            
                
            if j == m - 1 - h and check == 0:
                check = 1
            elif i == n - 1 - h and check == 1:
                check = 2
            elif j == 0 + h and check == 2:
                check = 3
            elif i == 1 + h and check == 3:
                check = 0
                h +=1
            
            
        print(spiral)
        return spiral
        