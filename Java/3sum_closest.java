class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        int min=Integer.MAX_VALUE;
        if(nums==null || nums.length<3)
            return 0;
        int sum=0,diff=0,ans=0;
        int low;
        int high;
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i++)
        {
            low=i+1;
            high=nums.length-1;
            
            while(low<high)
            {
                sum=nums[i]+nums[low]+nums[high];
                diff=Math.abs(sum-target);
                if(diff<min)
                {
                    min=diff;
                    ans=sum;
                }
                if(sum>target)
                    high--;
                else
                    low++;
            }
        }
        return ans;
        /*int diff=0,ans=0;
        Iterator<Integer> itr = set.iterator();
        while(itr.hasNext())
        {
            int setnum=itr.next();
            diff=Math.abs(setnum-target);
            if(diff<min)
            {
                min=diff;
                ans=setnum;
            }
        }*/
        //System.out.println(set);
        
    }
}