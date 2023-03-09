class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        ans = [0,0]
        for i in range(len(nums)):
            h[nums[i]] = i
        print(h)
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in h and h[complement] != i:
                ans[0] = i
                ans[1] = h[complement]
        
        return ans