class Solution:
    def maximumSwap(self, num: int) -> int:
        if num == 0:
            return 0
        l: list[int] = []
        while num > 0:
            l.append(num % 10)
            num //= 10
        l = l[::-1]
        #print(l)
        currMax = l[:]
        index = len(l) - 1
        for i in range(len(l) - 2, -1, -1):
            #print(i, index, currMax)
            if l[i] < l[index]:
                currMax = l[:]
                currMax[i],currMax[index] = currMax[index], currMax[i]
            elif l[i] > l[index]:
                index = i
        return int("".join([str(x) for x in currMax]))