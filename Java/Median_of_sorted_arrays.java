class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        //O(n+m)approach
        /*int nums3[]=new int[nums1.length+nums2.length];
        int i=0,j=0,k=0;
        
        while(i<nums1.length && j<nums2.length)
        {
            if(nums1[i]<nums2[j])
                nums3[k++]=nums1[i++];
            else
                nums3[k++]=nums2[j++];
        }
        while(i<nums1.length)
            nums3[k++]=nums1[i++];
        
        while(j<nums2.length)
            nums3[k++]=nums2[j++];
        
        
        double median=0.0;
        int half=(nums3.length/2);
        
            if(nums3.length % 2 == 0)
            {
                median=((double)nums3[half]+((double)nums3[half-1]))/2;
            }
            else
            {
                median=nums3[half];
            }
        
        
        return median;*/
        
        //O(log(m+n)) approach
        
        if(nums1.length > nums2.length)
            return findMedianSortedArrays(nums2,nums1);
        
        int x=nums1.length;
        int y=nums2.length;
        
        int low=0;
        int high=x;
        
        while(low<=high)
        {
            int partitionX=(low+high)/2;
            int partitionY=(x+y+1)/2 - partitionX;
            
            int maxLeftX = (partitionX==0) ? Integer.MIN_VALUE : nums1[partitionX-1];
            int minRightX = (partitionX==x) ? Integer.MAX_VALUE : nums1[partitionX];
            
            int maxLeftY = (partitionY==0) ? Integer.MIN_VALUE : nums2[partitionY-1];
            int minRightY = (partitionY==y) ? Integer.MAX_VALUE : nums2[partitionY];
            
            if(maxLeftX <= minRightY && maxLeftY <= minRightX)
            {
                if((x+y)%2 == 0)
                {
                    return ((double)Math.max(maxLeftX,maxLeftY) + Math.min(minRightX,minRightY))/2;
                }
                else
                {
                    return ((double)Math.max(maxLeftX,maxLeftY));
                }
            }
            else if(maxLeftX > minRightY)
            {
                high=partitionX-1;
            }
            else
            {
                low=partitionX+1;
            }
        }
        
        throw new IllegalArgumentException();
    }
}