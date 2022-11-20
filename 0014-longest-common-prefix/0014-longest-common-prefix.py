class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        for i in zip(*strs):
            #print("".join(set(i)), i)
            strs = "".join(set(i))
            if len(strs) == 1: 
                ans += strs
            else:
                break
                
        return ans