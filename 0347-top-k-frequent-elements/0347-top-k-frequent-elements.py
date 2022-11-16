class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
        sorted_hashmap = {k : v for k, v in sorted(hashmap.items(), key = lambda x:x[1], reverse = True)}        
        
        ans = []
        
        for key in sorted_hashmap.keys():
            if k > 0:
                ans.append(key)
                k -= 1
                
        return ans