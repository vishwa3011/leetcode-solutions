class Solution {
    public int firstMissingPositive(int[] nums) {
        
        /*Set <Integer> set = new HashSet<>();
        for(int i=0;i<nums.length;i++)
        {
            set.add(nums[i]);
        }
        
        if(!set.contains(1))
                return 1;
        
        for(int i=1;i<nums.length+1;i++)
        {
            if(!set.contains(i))
                return i;
        }
        return nums.length+1;*/
        
        
        /*int arr[]=new int[nums.length+1];
        
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]>0 && nums[i]<=nums.length)
                arr[nums[i]]++;
        }
        for(int i=1;i<arr.length;i++)
        {
            if(arr[i]==0)
                return i;
        }
        return arr.length;*/
        
        //O(1) space
        for(int i=0;i<nums.length;i++)
        {
            while(nums[i]>0 && nums[i]<=nums.length && nums[nums[i]-1] != nums[i])
            {   //placing numbers wrt their indices
                int temp=nums[nums[i]-1];
                nums[nums[i]-1]=nums[i];
                nums[i]=temp;
            }
        }
        //checking whether that number is equal to its index or not
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]!=i+1)
                return i+1;
        }
        return nums.length+1;
    }
}