class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> li = new ArrayList<>();
        
        Arrays.sort(nums);
        int sum;
        Set<List<Integer>> setlist = new HashSet<>();
        
        if(nums==null || nums.length<3)
            return li;
        /*Approach1
        Set<Integer> set = new HashSet<>();
        for(int i=0;i<nums.length;i++)
        {
            set.add(nums[i]);
        }
        //System.out.print(set);
        for(int i=0;i<nums.length;i++)
        {
           for(int j=0;j<nums.length;j++)
            {
               if(i!=j)
               {
                   sum=(nums[i]+nums[j])*(-1);
                   
                   if(set.contains(sum) && sum!=nums[i] && sum!=nums[j])
                   {
                       setlist.add(Arrays.asList(nums[i],nums[j],sum));  
                   }
               }
            }
            
        }*/
        
        /*Approach2
        int index=1;
        int left,right;
        
        while(index<nums.length)
        {
            left=index-1;
            right=index+1;
            while(left>=0 && right<nums.length)
            {
                sum=nums[left]+nums[index]+nums[right];
                if(sum==0)
                {
                    setlist.add(Arrays.asList(nums[left],nums[index],nums[right]));
                    right++;
                    left--;
                }
                else if(sum<0)
                    right++;
                else
                    left--;
            }
            index++;
        }*/
        //Approach3
        int low,high;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]>0)
                break;
            if(i>0 && nums[i]==nums[i-1])
                continue;//skip the equal elements
            low=i+1;
            high=nums.length-1;
            while(low<high)
            {
                if(nums[low]+nums[high]==(-nums[i]))
                {
                    setlist.add(Arrays.asList(nums[i],nums[low],nums[high]));
                    //while(low<high && nums[low]==nums[low+1]) low++;
                    low++;
                    //while(low<high && nums[high]==nums[high-1]) high--;
                    high--;
                }
                else if(nums[low]+nums[high]>(-nums[i]))
                {
                    //while(low<high && nums[high]==nums[high-1]) high--;
                    high--;
                }
                else
                {
                    //while(low<high && nums[low]==nums[low+1]) low++;
                    low++;
                }
                    
            }
        }
        li.addAll(setlist);
        return li;
    }
}