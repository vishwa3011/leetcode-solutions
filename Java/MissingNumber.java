class Solution {
    public int missingNumber(int[] nums) {
        
        /*int ans=0;
        int j=0;
        Arrays.sort(nums);
        
        if(nums[nums.length-1] != nums.length)
            ans=nums.length;
        else if(nums[0] != 0)
            ans=0;
        else
        {
            for(int i=1;i<nums.length;i++)
            {
                j=nums[i-1]+1;
                if(nums[i] != j)
                    ans=j;
            }
        }
        
        return ans;*/
        
        /*Set<Integer> set = new HashSet<>();
        
        for(int num:nums)
        {
            set.add(num);
        }
        
        for(int i=0;i<nums.length+1;i++)
        {
            if(!set.contains(i))
                return i;
        }
        
        return -1;*/
        int max=nums[0];
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]>max)
                max=nums[i];
        }
        
        int arr[]=new int[max==0?1:max+1];
        
        for(int i=0;i<nums.length;i++)
        {
            arr[nums[i]]++;
        }
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]==0)
                return i;
        }
        return arr.length;
    
}
}