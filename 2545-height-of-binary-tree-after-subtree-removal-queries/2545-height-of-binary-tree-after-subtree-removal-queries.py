# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heightsOfSubtrees: dict[int, int] = {}
        levels: list[list[int]] = list()
        rootValLevelDict: dict[int, int] = {}
        self.getHeights(root, heightsOfSubtrees, levels, 1, rootValLevelDict)
        #print(rootValLevelDict)
        sorted_root_valsByHeightOfSubtree: list[list[tuple[int]]] = [[] for _ in range(len(levels))]
        
        for key, value in heightsOfSubtrees.items():
            index = rootValLevelDict[key]
            ixInList = bisect_left(sorted_root_valsByHeightOfSubtree[index],value, key = lambda x: x[1])
            sorted_root_valsByHeightOfSubtree[index].insert(ixInList, (key, value))
        
        print(sorted_root_valsByHeightOfSubtree)
        result: list[int] = list()
        for query in queries:
            result.append(self.calculateMaxHeightAfterDeletion(sorted_root_valsByHeightOfSubtree, rootValLevelDict, query))
        return result
    def getHeights(self, root, hashmap, levels, currLevel, rootValLevelDict):
        if root is None:
            return -1
        if currLevel > len(levels):
            levels.append([])
        levels[currLevel - 1].append(root.val)
        rootValLevelDict[root.val] = currLevel - 1
        l = 1 + self.getHeights(root.left, hashmap, levels, currLevel + 1, rootValLevelDict)
        r = 1 + self.getHeights(root.right, hashmap, levels, currLevel + 1, rootValLevelDict)
        hashmap[root.val] = max(l, r)
        return max(l, r)
    
    def calculateMaxHeightAfterDeletion(self, sorted_root_valsByHeightOfSubtree, rootValLevelDict, query):
        index = rootValLevelDict[query]
        treeHeight = sorted_root_valsByHeightOfSubtree[0][0][1]
        if len(sorted_root_valsByHeightOfSubtree[index]) == 1:
            return treeHeight - sorted_root_valsByHeightOfSubtree[index][0][1] - 1
        if sorted_root_valsByHeightOfSubtree[index][-1][0] == query:
            return treeHeight - (sorted_root_valsByHeightOfSubtree[index][-1][1] - sorted_root_valsByHeightOfSubtree[index][-2][1])
        
        return treeHeight