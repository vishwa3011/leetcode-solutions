class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s)
        l = 0
        while n > 0:
            n -= 1
            
            if s[n] != ' ':
                l += 1
            elif l > 0:
                return l
         
        return l
            
        #list_strings = s.strip().split(" ")
        #return len(list_strings[-1])