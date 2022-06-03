class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        i = 0
        j = len(nums)-1
        k = j
        arr = [0]*len(nums)
        
        while i <= j:
            
            if abs(nums[i]) > abs(nums[j]):
                arr[k] = nums[i]**2
                i += 1
            else:
                arr[k] = nums[j]**2
                j -= 1
            k -= 1
        
        return arr