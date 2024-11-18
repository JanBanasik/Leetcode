class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * len(code)
        
        sign = None
        if k > 0:
            left = 0
            right = n
            sign = 1
            code = code + code[0:k]
        else:
            left = -k
            right = -k + n
            sign = -1
            code = code[k:] + code
        res = []
        for i in range(left, right):


            if k > 0:
                res.append(sum(code[i+1:i+k+1]))
            else:
                res.append(sum(code[i + k:i]))
        return res