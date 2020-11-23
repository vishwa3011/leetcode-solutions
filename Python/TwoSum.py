class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum_dict={}   #{element:index}
        
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in twosum_dict:
                return (i,twosum_dict[compliment])
            else:
                twosum_dict[num]=i
        
        
        