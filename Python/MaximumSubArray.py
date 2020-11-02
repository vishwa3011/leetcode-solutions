class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_final=nums[0]
        max_till_here=0
        
        for num in nums:
            max_till_here=max(num,max_till_here+num)
            max_final=max(max_final,max_till_here)
        
        return max_final