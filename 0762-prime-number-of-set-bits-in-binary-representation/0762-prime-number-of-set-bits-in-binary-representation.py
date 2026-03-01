def ifprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3,n):
        if n % i == 0:
            return False
    return True
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        counter = 0
        for i in range(left,right+1):
            number = bin(i)
            s = str(number).count("1")
            if ifprime(s):
                counter +=1
        return counter