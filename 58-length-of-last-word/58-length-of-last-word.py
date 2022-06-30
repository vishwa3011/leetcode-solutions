class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        
        for c in reversed(s):
            if c == ' ':
                break
            count += 1
            
        return count