class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        allowedSetBits = bin(num2).count("1")
        result = str()
        for value in bin(num1)[2::]:
            if value == "1" and allowedSetBits > 0:
                allowedSetBits -=1
                result += "1"
            else:
                result += "0"
        if allowedSetBits > 0:
            result = list(result)
            for i in range(len(result) - 1, -1, -1):
                if result[i] == "0":
                    result[i] = "1"
                    allowedSetBits -=1
                if allowedSetBits == 0:
                    break
            result = "".join(result)
        while(allowedSetBits > 0):
            result += "1"
            allowedSetBits -=1
        return int(result, 2)