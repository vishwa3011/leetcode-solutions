class Solution {
    public int maxSubArray(int[] nums) {
        
        
        
        int max_final=nums[0];
        int max_till_here=0;
        for(int i=0;i<nums.length;i++)
        {
            //max_till_here=max_till_here+nums[i];
            max_till_here=Math.max(max_till_here+nums[i],nums[i]);
            
            max_final = Math.max(max_final,max_till_here);
            /*if(max_till_here<0) //if the sum is less than zero than reset(another approach)
            {
                max_till_here=0;
            }*/
        }
        return max_final;
    }
}