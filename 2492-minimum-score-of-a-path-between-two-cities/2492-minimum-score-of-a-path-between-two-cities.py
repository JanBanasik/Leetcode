#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, score in roads:
            graph[u].append((v, score))
            graph[v].append((u, score))
        
        min_score = float('inf')
        visited = set()

        queue = deque([1])
        visited.add(1)
        while queue:
            node = queue.popleft()
            for neighbor, score in graph[node]:
                min_score = min(min_score, score)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return min_score
# @lc code=end

