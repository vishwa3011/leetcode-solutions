class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        1) flip the index sign for a specific number in the list
        '''
        for i in nums:
            current = abs(i)
            if nums[current] < 0:
                return current
            nums[current] = -nums[current]
        
        
        return -1
                
#         dups = {}
        
#         for i in nums:
#             if i not in dups:
#                 dups[i] = 1
#             else:
#                 dups[i] += 1
        
#         for key,val in dups.items():
#             if val > 1:
#                 return key
        
#         return -1