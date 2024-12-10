class Solution:
    def maximumLength(self, s: str) -> int:
        c = 1
        specials = []
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                specials.append(s[i-1]*c)
                c = 0
            c +=1
        specials.append(s[-1]*c)
        hashmap = defaultdict(int)
        for special in specials:
            n = len(special)
            for i in range(n):
                hashmap[special[0] * (i + 1)] += (n-i)
        
        m = -1
        for sub, length in sorted(hashmap.items(), key = lambda x:x[1]):
            if length >= 3:
                m = max(m, len(sub))
        return m