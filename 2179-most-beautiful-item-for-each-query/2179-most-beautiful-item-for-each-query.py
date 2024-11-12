import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        hashmap = {}
        for price, beauty in items:
            hashmap[price] = max(hashmap.get(price, 0), beauty)
        hashmap = sorted(list(hashmap.items()), key = lambda x : x[0])
        hashmap = [list(x) for x in hashmap]
        for i in range(1, len(hashmap)):
            hashmap[i][1] = max(hashmap[i][1], hashmap[i - 1][1])
        res = []
        pierwsze_elementy = [x[0] for x in hashmap]
        for query in queries:
            ix = self.znajdz_indeks(pierwsze_elementy, query)
            if ix is None:
                res.append(0)
            else:
                res.append(hashmap[ix][1])
        return res
    
    def znajdz_indeks(self, pierwsze_elementy, target):
        
        indeks = bisect_right(pierwsze_elementy, target) - 1
        return indeks if indeks >= 0 else None