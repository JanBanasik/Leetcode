class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        h = {}
        for k, v in knowledge:
            h[k] = v
        
        result: str = ""

        flag = False
        k = str()
        for c in s:

            if c == "(":
                flag = True
                continue

            if not flag:
                result += c
            
            else:
                if c == ")":
                    flag = False
                    result += h.get(k, "?")
                    k = ""
                else:
                    k += c
            
            
        return result