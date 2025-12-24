class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        packsSum: int = sum(apple)
        capacity.sort(reverse=True)
        ix: int = 0
        while packsSum > 0:
            packsSum -= capacity[ix]
            ix +=1
        return ix