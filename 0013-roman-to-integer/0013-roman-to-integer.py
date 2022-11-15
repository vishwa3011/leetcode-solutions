class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashmap = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        integer = 0
        
        i = 0
        
        while i < len(s):
            
            if i < len(s) - 1:
                if i < len(s) - 1 and (s[i] == 'I' and s[i+1] == 'V') or (s[i] == 'I' and s[i+1] == 'X') or (s[i] == 'X' and s[i+1] == 'L') or (s[i] == 'X' and s[i+1] == 'C') or (s[i] == 'C' and s[i+1] == 'D') or (s[i] == 'C' and s[i+1] == 'M'):
                    integer += hashmap[s[i+1]] - hashmap[s[i]]
                    i += 1
                else:
                    integer += hashmap[s[i]]
            else:
                integer += hashmap[s[i]]
            
            i += 1
            
        return integer