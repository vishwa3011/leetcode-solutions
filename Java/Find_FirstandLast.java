class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        /*List<Integer> li = new ArrayList<>();
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==target)
            {
                li.add(i);
            }
        }
        if(li.isEmpty())
            return new int[] {-1,-1};
        for(int i=0;i<li.size();i++)
        {
            return new int[] {li.get(0),li.get(li.size()-1)};
        }
        throw new IllegalArgumentException("No solution");*/
        
        int leftIndex = binarySearchLeft(nums, target, true);
        int rightIndex = binarySearchLeft(nums, target, false);
        
        return new int[]{leftIndex, rightIndex};
    }

    public int binarySearchLeft(int[] nums, int target, boolean isLeft) {
        
            int low=0;
            int high=nums.length-1;
            int index=-1;
            while(low<=high)
            {
                int mid=low+(high-low)/2;
                if(nums[mid]==target)
                {
                    index=mid;
                    if(isLeft)
                        high=mid-1;
                    else
                        low=mid+1;
                }
                else if(nums[mid]>target)
                    high=mid-1;
                else
                    low=mid+1;
            }
        
        return index;
    }
}