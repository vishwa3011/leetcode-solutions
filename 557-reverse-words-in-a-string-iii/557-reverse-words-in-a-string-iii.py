class Solution:
    def reverseWords(self, s: str) -> str:
        
        ans = ""
        for i in s.split(" "):
            l = list(i)
            
            ans += " " + self.reverse(l)
        
        return ans.lstrip()
        
    def reverse(self, ls):
        i = 0
        j = len(ls)-1
        
        while i < j:
            ls[i],ls[j] = ls[j],ls[i]
            i += 1
            j -= 1
        
        return ''.join(ls)