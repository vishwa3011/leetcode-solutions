class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        max_sub_str = ""
        
        for windowEnd in range(len(s)):
            
            for windowStart in range(windowEnd + 1):
                
                curr_str = s[windowStart:windowEnd+1] 
                
                if self.isNiceSubstring(curr_str):
                    max_sub_str = max(max_sub_str, curr_str, key = len)
        
        return max_sub_str
    
    
    def isNiceSubstring(self, string):
        chars = set(string)
        
        for char in chars:
            
            validchars = char.upper() in chars and char.lower() in chars
            
            if not validchars:
                return False
        
        return True