class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        
        while i != len(nums) and j != len(nums):
            
            if nums[i] == 0 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == nums[j]:
                j += 1
            else:
                i += 1
        
        return nums