class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        tab = [1 if x[0] in vowels and x[-1] in vowels else 0 for x in words]
        cumSum = [0]
        for val in tab:
            cumSum.append(cumSum[-1] + val)
        
        return [cumSum[b + 1] - cumSum[a] for a, b in queries]
