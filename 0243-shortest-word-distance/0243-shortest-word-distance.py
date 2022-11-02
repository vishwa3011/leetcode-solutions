class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        shortest_distance = len(wordsDict)
        idx1, idx2 = -1, -1
        for idx, word in enumerate(wordsDict):
            
            if word1 == word:
                idx1 = idx
            elif word2 == word:
                idx2 = idx
            
            if idx1 != -1 and idx2 != -1:
                shortest_distance = min(shortest_distance, abs(idx1 - idx2))
        
        return shortest_distance
            