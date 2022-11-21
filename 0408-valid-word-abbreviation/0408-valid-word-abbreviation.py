class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i, j = 0, 0
        
        while i < len(word) and j < len(abbr):
            
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                idx = 0
                if abbr[j] == '0':
                    return False
                while j < len(abbr) and abbr[j].isdigit():
                    idx = idx * 10 + int(abbr[j])
                    j += 1
                
                i += idx
        
        
        return i == len(word) and j == len(abbr)