class Solution:
    
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)

        if n == 1:
            return bits[0] == 0
        
        lastTwo = bits[-2:]

        if lastTwo == [0, 0]:
            return True
        
        i = n - 3

        while i >= 0:
            if i == 0 and bits[i] == 1:
                return True
            
            if bits[i - 1] == 1:
                i-=2
            else:
                if bits[i] == 1:
                    return True
                i -=1
        return False

        