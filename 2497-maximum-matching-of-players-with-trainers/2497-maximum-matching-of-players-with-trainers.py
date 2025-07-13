class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        result: int = 0
        ix: int = 0
        i: int = 0
        
        while i < len(players) and ix < len(trainers):
            if players[i] <= trainers[ix]:
                result +=1
                i +=1
            ix +=1
        return result