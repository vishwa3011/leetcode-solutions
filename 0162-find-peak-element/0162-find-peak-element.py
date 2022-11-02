class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low < high - 1:
            mid = (low + high)//2
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
            
        if nums[low] >= nums[high]:
            return low
        else:
            return high