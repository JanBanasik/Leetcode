class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        onesPositionSet = set()
        for index, value in enumerate(boxes):
            if value == "1":
                onesPositionSet.add(index)
        
        answer = []
        for i in range(len(boxes)):
            moves = self.calculateMoves(i, onesPositionSet)
            answer.append(moves)
        return answer

    def calculateMoves(self, i, onesPositionSet):
        moves = 0
        for value in onesPositionSet:
            moves += abs(i - value)
        return moves