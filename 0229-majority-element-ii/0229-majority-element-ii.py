import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashmap = {}
        n = math.floor(len(nums)/3)
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        ans = []
        print(hashmap, n)
        for key, val in hashmap.items():
            if val > n:
                ans.append(key)
        
        return ans