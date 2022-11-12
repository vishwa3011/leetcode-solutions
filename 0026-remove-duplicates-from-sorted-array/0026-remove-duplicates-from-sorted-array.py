class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i, j = 0, 0
        
        while j < len(nums) - 1:
            while nums[i] == nums[j]:
                j += 1
                if j == len(nums):
                    break
            
            if j == len(nums):
                break
            i += 1
            nums[i] = nums[j]
            
        
        return i+1
        
        