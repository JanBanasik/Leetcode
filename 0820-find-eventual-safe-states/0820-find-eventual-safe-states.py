class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answer = set()
        convertedGraph = defaultdict(list)
        for index, value in enumerate(graph):
            for el in value:
                convertedGraph[el].append(index)
        graph = [len(x) for x in graph]
        found = False
        while True:
            found = False
            for index, value in enumerate(graph):
                if value == 0 and index not in answer:
                    found = True
                    answer.add(index)
                    for element in convertedGraph[index]:
                        graph[element] -=1
                    
            if not found:
                break

        return sorted(list(answer))