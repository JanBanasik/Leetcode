class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        ix = self.findIx(self.arr, num)
        self.arr.insert(ix, num)

    def findMedian(self) -> float:
        
        n = len(self.arr)
        if n % 2 == 0:
            return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2
        else:
            return self.arr[n // 2]

    def findIx(self, arr, num):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid] == num:
                return mid
            elif arr[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        return left
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()