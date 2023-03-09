class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = 1
            else:
                h[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] in h:
                h[t[i]] -= 1
        
        print(h)
        
        for val in h.values():
            if val != 0:
                return False
        
        return True
            
        