class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = sorted(meetings, key = lambda x: x[2])
        hashmap = {}
        # hashmap[i] = x1: [y1,y2,y3] # czyli o czasie tym i tym spotyka sie jakas osoba i lista z kim sie spotyka
        print(meetings)
        for p1, p2,time in meetings:
            if time not in hashmap:
                hashmap[time] = []
            flag = False
            for meeting in hashmap[time]:
                if p1 in meeting or p2 in meeting:
                    meeting.add(p1)
                    meeting.add(p2)
                    flag = True
                    break
            if not flag:
                hashmap[time].append(set([p1,p2]))
            

        
        has_secret = set()
        has_secret.add(0)
        has_secret.add(firstPerson)
        for key, value in hashmap.items():
            it = 1
            found = False
            for x in range(len(value)):
                for meeting in value:
                    if len(has_secret.intersection(meeting)) != 0:
                        for person in meeting:
                            has_secret.add(person)
        return list(has_secret)