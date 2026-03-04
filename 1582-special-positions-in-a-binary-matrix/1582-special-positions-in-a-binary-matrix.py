class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special = 0
        for i in range(len(mat)):
            if mat[i].count(1) == 1:
                ix = mat[i].index(1)
                flag = True
                for j in range(len(mat)):
                    if j != i:
                        if mat[j][ix] == 1:
                            flag = False
                            break
                if flag:
                    special +=1
        return special