class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                h[nums[i]] += 1
        
        for val in h.values():
            if val > 1:
                return True
        
        return False