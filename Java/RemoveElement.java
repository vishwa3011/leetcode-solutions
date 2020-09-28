class Solution {
    public int removeElement(int[] nums, int val) {
        
        int count=0;
        
        int i=0,j=0;
        
        while(i<nums.length)
        {
            if(nums[i]!=val)
            {
                count++;
                //int temp=nums[j];
                nums[j]=nums[i];
                //nums[i]=temp;
                j++;
            }
            i++;
        }
       return count;
    }
}