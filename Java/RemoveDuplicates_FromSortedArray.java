class Solution {
    public int removeDuplicates(int[] nums) {
        
        int i=0; //int j=1;
        int count=0;
        
        /*for(int k=0;k<nums.length-1;k++)
        {
            if(nums[k]==nums[k+1])
                count++;
        }
        
        while(i<nums.length-1)
        {
            if(nums[i]!=nums[i+1])
            {
                nums[j]=nums[i+1];
                j++;
            }
            i++;
        }
        
        return nums.length-count;*/
        
        for(int j=1;j<nums.length;j++)
        {
            if(nums[j]!=nums[i])
            {
                i++;
                nums[i]=nums[j];
            }
        }
        return i+1;
    }
}