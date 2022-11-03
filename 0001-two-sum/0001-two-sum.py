class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        two_sum_dict = {}
        ans = [0, 0]
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in two_sum_dict:
                return [i, two_sum_dict[complement]]
            
            two_sum_dict[nums[i]] = i
        
        return [-1,-1]