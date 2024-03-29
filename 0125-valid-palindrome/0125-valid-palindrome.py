class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s or s == ' ':
            return True
        
        reverse_string = ""
        input_string = ""
        
        s = s.lower()
        i, j = 0, len(s)-1
        
        while i < len(s) and j >= 0:
            if s[i].isalnum():
                input_string += s[i]
            
            i += 1
            
            if s[j].isalnum():
                reverse_string += s[j]
            
            j -= 1
                    
        return input_string == reverse_string