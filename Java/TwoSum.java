import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for(int i=0;i<nums.length;i++)
        {
            int complement=target-nums[i];
            if(map.containsKey(complement))
            {
                   // ans[0]=map.get(nums[i]);
                    //ans[1]=i;
                return new int[] { map.get(complement),i };
                
            }
            map.put(nums[i],i);
            
        }
        
         throw new IllegalArgumentException("No two sum solution");
        
}
}