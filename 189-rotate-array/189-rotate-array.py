class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        nums = self.swap(0, len(nums)-1, nums)
        nums = self.swap(0, k-1, nums)
        nums = self.swap(k, len(nums)-1, nums)
        
    def swap(self, i, j, nums):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1  
        return nums
        
            
            
#         rotated_arr = []
#         n = len(nums)
#         temp = k
#         while temp > 0:
#             rotated_arr.append(nums[n - temp])
#             temp -= 1
        
#         i = 0
#         while i <= k:
#             rotated_arr.append(nums[i])
#             i += 1
        
#         print(rotated_arr)
            