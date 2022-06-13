class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        dups = {}
        
        for i in nums:
            if i not in dups:
                dups[i] = 1
            else:
                dups[i] += 1
        print(dups)
        
        for key,val in dups.items():
            if val > 1:
                return key
        
        return -1