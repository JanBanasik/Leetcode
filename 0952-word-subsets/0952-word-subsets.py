class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words, subsets = self.countWords(words1), self.countMaxFreq(words2)
        result = []
        for index, wordDict in enumerate(words):
            flag = True
            for key, value in subsets.items():
                if value > wordDict[key]:
                    flag = False
                    break
            if flag:
                result.append(words1[index])
        return result
    def countWords(self, words) -> list[defaultdict(int)]:
        result = list()
        for word in words:
            temp = defaultdict(int)
            for c in word:
                temp[c] +=1
            result.append(temp)
        return result
    
    def countMaxFreq(self, words):
        result = defaultdict(int)
        for word in words:
            temp = defaultdict(int)
            for c in word:
                temp[c] +=1
            for key, value in temp.items():
                result[key] = max(result[key], value)
        return result
