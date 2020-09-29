class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        //HashMap<Integer,Integer> map = new HashMap<>();
        
        /*for(int i=0;i<nums.length;i++)
        {
            if(!map.containsKey(nums[i]))
                map.put(nums[i],0);
            
            map.put(nums[i],map.get(nums[i])+1);
        }*/
        /*for(int num:nums)
        {
            map.put(num,map.getOrDefault(num,0)+1);
        }
        for(Map.Entry<Integer,Integer> entry : map.entrySet())
        {
            if(entry.getValue()>1)
                return true;
        }
        return false;*/
        
        Set<Integer> set = new HashSet<>();
        for(int i:nums)
        {
            if(!set.add(i))
                return true;
            //set.add(i);
        }
        return false;
    }
}