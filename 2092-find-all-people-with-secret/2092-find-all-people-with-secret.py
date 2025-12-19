class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = sorted(meetings, key = lambda x: x[2])
        hashmap = {}
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
            for x in range(len(value)):
                for meeting in value:
                    if len(has_secret.intersection(meeting)) != 0:
                        for person in meeting:
                            has_secret.add(person)
        return has_secret