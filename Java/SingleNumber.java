class Solution {
    public int singleNumber(int[] nums) {
        
        
        HashMap<Integer,Integer> map=new HashMap<>();
        int ans=0;
        for(int i=0;i<nums.length;i++)
        {
            map.put(nums[i],0);
        }
        int count=0;
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                map.put(nums[i],map.get(nums[i])+1);
            } 
        }
        for(int i=0;i<nums.length;i++)
        {
            if(map.get(nums[i])==1)
                ans=nums[i];
        }
        return ans;
        
        /*int xor=nums[0]; //Faster approach
        for(int i=1;i<nums.length;i++)
        {
            xor=xor^nums[i];
        }
        return xor;*/
        
       
    }
}