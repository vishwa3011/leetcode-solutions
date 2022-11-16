from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_anagrams = defaultdict(list)
        ans = []
        
        for word in strs:
            count_chars = [0]*26
            for char in word:
                count_chars[ord(char) - ord('a')] += 1
            group_anagrams[tuple(count_chars)].append(word)
        
        return list(group_anagrams.values())
    
        ## Brute Force (gives TLE for big inputs)
#         ans = []
#         idx = []
        
#         for i in range(len(strs)):
#             anagrams = []
#             if i not in idx:
#                 anagrams.append(strs[i])
#                 for j in range(len(strs)):
#                     if j not in idx:
#                         if Counter(strs[i]) == Counter(strs[j]) and i != j:
#                             anagrams.append(strs[j])
#                             idx.append(j)
                    
#                 ans.append(anagrams)
        
#         return ans