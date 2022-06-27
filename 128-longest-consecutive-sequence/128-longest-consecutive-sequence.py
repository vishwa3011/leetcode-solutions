class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        num_set = set(nums)
        max_consec = 0
        consec = 0
        
        for num in nums:
            if num - 1 not in num_set:
                curr_num = num
                consec = 1
            
                while curr_num + 1 in num_set:
                    consec += 1
                    curr_num += 1
            
                max_consec = max(max_consec, consec)
        
        return max_consec