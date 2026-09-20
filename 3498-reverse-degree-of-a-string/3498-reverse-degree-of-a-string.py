class Solution:
    def reverseDegree(self, s: str) -> int:
        hashmap = {}

        for i in range(0, 27):
            hashmap[chr(i + 97)] = 26 - i
        
        return sum(index * hashmap[val] for index, val in enumerate(s, 1))