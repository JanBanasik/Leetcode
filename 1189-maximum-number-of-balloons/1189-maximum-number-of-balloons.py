from typing import List

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter: List[int] = [0] * 26
        
        for c in text:
            counter[ord(c) - 97] +=1
        
        return min([counter[ord(c) - 97] if c not in 'lo' else counter[ord(c) - 97] // 2 for c in 'balon'])
        