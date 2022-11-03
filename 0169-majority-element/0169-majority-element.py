class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counts = {}
        
        for i in range(len(nums)):
            if nums[i] not in num_counts:
                num_counts[nums[i]] = 1
            else:
                num_counts[nums[i]] += 1
            
        for key, val in num_counts.items():
            if val > len(nums)/2:
                return key
        
        return -1