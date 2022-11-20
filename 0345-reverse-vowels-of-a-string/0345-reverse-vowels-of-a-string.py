class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        #s = s.lower()
        
        i, j = 0, len(s)-1
        ls = list(s)
        
        while i <= j:
            if ls[i] in vowels and ls[j] in vowels:
                ls[i], ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
            elif ls[i] in vowels and ls[j] not in vowels:
                j -= 1
            elif ls[i] not in vowels and ls[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
                
        return "".join(ls)