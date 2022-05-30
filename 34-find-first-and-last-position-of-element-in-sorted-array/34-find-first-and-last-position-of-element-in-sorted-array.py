class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        '''
        We will use binary search for this problem to achieve O(log n) complexity
        '''
        
        start = self.binary_search(nums, target, 0, len(nums)-1, isFirst = True)
        end = self.binary_search(nums, target, 0, len(nums)-1, isFirst = False)
        
        if start == -1 or end == -1:
            return [-1,-1]
        else:
            return [start, end]
        
    
    def binary_search(self, nums, target, low, high, isFirst):
        
        ans = []
        while low <= high:
            
            mid = low + (high - low)//2
            if target == nums[mid]:
                if isFirst:
                    if mid == low or nums[mid - 1] != target:
                        return mid
                    else:
                        high = mid - 1
                else:
                    if mid == high or nums[mid + 1] != target:
                        return mid
                    else:
                        low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1