class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        List<Integer> ans = new ArrayList<>();
        int i=0;
        while(i<nums.length)
        {
            int curr = nums[i];//taking the element and placing it in its right position
            while(nums[curr-1] != curr)
            {
                int t = nums[curr-1];
                nums[curr-1] = curr;
                curr = t;
            }
            i++;
        }
        
        for(int j=0;j<nums.length;j++)
        {
            if(nums[j]!=j+1)
                ans.add(j+1);
        }
        return ans;
        
    }
}