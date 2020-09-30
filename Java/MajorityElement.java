class Solution {
    public int majorityElement(int[] nums) {
        
        HashMap<Integer,Integer> map=new HashMap<>();
        
        for(int i:nums)
        {
            map.put(i,map.getOrDefault(i,0)+1);
        }
        for(int i=0;i<nums.length;i++)
        {
            if(map.get(nums[i]) > nums.length/2)
                return nums[i];
        }
        return -1;
         //Boyer-Moore Voting Algorithm
         /*(int count = 0;
         Integer candidate = null;
 
         for (int num : nums) {
             if (count == 0) {
                 candidate = num;
             }
             count += (num == candidate) ? 1 : -1;
         }
 
         return candidate;*/
    }
}