class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        
        List<List<Integer>> li = new ArrayList<>();
        
        if(nums==null || nums.length<4)
            return li;
        Arrays.sort(nums);
        int low,high,mid;
        
        //Set<List<Integer>> setlist = new HashSet<>();
        for(int i=0;i<nums.length-3;i++)
        {
            if (i > 0 && nums[i] == nums[i - 1]) 
                continue;
            for(int j=i+1;j<nums.length-2;j++)
            {
                if (j > i + 1 && nums[j] == nums[j - 1]) 
                    continue;
                low=j+1;
                high=nums.length-1;
                while(low<high)
                {
                    if(nums[i]+nums[low]+nums[j]+nums[high]==target)
                    {
                        li.add(Arrays.asList(nums[i],nums[j],nums[low],nums[high]));
                        low++;
                        high--;
                        while(low<high && nums[low]==nums[low-1]) low++;
                        while(low<high && nums[high]==nums[high+1]) high--;
                        
                    }
                    else if(nums[i]+nums[low]+nums[j]+nums[high]>target)
                    {
                        high--;
                    }
                    else
                    {
                        low++;
                    }

                }
            }
        }
        //li.addAll(setlist);
        return li;
    }


}
    