class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = low + (high-low)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        # If element is not present
        idx = 0
        for i in nums:
            if i < target:
                idx += 1
        
        return idx
            