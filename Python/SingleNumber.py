class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict=defaultdict(int)
        
        '''for num in nums:
            my_dict[num]=my_dict.get(num,0)+1'''
        
        for num in nums:
            my_dict[num]+=1
        
        
        for i in my_dict:
            if my_dict[i] == 1:
                return i
            
    '''
    for i in nums:
        if nums.count(i)==1:
            return i
    '''