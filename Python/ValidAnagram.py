class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        anagram=defaultdict(int)
        
        for ss in s:
            anagram[ss]+=1
        
        for tt in t:
            anagram[tt]-=1
        
        for i in anagram:
            if anagram[i]!=0:
                return False
        
        return True  
        #return sorted(s) == sorted(t)