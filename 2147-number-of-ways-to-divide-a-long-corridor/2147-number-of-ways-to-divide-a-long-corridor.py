class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') % 2 == 1 or corridor.count('S') == 0:
            return 0 
        if corridor.count('S') == 2:
            return 1
        mod = 10**9 + 7
        counts = []
        counter = 0
        plants = []
        p = 0
        while corridor[0] == 'P':
            corridor = corridor[1::]
        for i in corridor:
            if i == 'S':
                counter +=1
                if counter == 1 and plants:
                    plants.append(p+1)
                    p = 0
               
                if counter == 4:
                    plants.append(p + 1)
                    p = 0
                    counter = 0
            else:
                if counter == 2 or counter == 0:
                    p +=1
        res = 1
        for i in plants:
            res *= i
        return res % mod