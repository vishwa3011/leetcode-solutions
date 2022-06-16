class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        We can store the element as key and its complement as value in a dictionary
        '''
        
        two_sum_dict = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in two_sum_dict:
                return [i, two_sum_dict[complement]]
            
            two_sum_dict[nums[i]] = i
            
        print(two_sum_dict)
        
        return -1