class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        chars = [0]*26
        
        for i in ransomNote:
            chars[ord(i) - ord('a')] += 1
        
        print(chars)
        for i in magazine:
            chars[ord(i) - ord('a')] -= 1
        
        print(chars)
        
        for i in chars:
            if i > 0:
                return False
        
        return True