from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ## use sliding window technique
        ## dynamic resizing and auxillary data structure needed
        
        
        windowStart, windowEnd = 0, 0
        hashmap = Counter()
        max_len = 0
        
        while windowEnd < len(s):
            curr_char = s[windowEnd]
            hashmap[curr_char] += 1
            
            
            while hashmap[curr_char] > 1:
                left = s[windowStart]
                hashmap[left] -= 1
                windowStart += 1
                
            max_len = max(max_len, windowEnd - windowStart + 1)
            
            windowEnd += 1
        
        return max_len
            
            
            
        
#         for windowEnd in range(len(s)):
#             for windowStart in range(windowEnd + 1):
#                 curr_str = s[windowStart : windowEnd + 1]
#                 if len(curr_str) == len(set(curr_str)):
#                     longest_substr = max(longest_substr, curr_str, key = len)
        
#         return len(longest_substr)