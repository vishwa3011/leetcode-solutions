class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time - O(n) Space - O(n)
#         num_counts = {}
        
#         for i in range(len(nums)):
#             if nums[i] not in num_counts:
#                 num_counts[nums[i]] = 1
#             else:
#                 num_counts[nums[i]] += 1
            
#         for key, val in num_counts.items():
#             if val > len(nums)/2:
#                 return key
        
#         return -1
    
        ## Boyer Moore Voting Algorithm
        # Time - O(n) Space - O(1)
        
        count = 0
        candidate = None
        
        for num in nums:
            
            if count == 0:
                candidate = num
                
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
        