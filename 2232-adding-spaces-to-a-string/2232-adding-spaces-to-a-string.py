class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = ""
        x = 0
        for i in range(len(s)):
            if i == spaces[x]:
                new_s+= f" {s[i]}"
                x +=1
                if x == len(spaces):
                    for k in range(i + 1, len(s)):
                        new_s += s[k]
                    return new_s
            else:
                new_s += s[i]
        return new_s