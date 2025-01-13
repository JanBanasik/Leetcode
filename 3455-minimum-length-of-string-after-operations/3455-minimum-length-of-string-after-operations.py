class Solution:
    def minimumLength(self, s: str) -> int:
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] +=1

        result: int = 0
        for key, value in hashmap.items():
            if value % 2 == 1:
                result += 1 
            else:
                result += 2
        return result