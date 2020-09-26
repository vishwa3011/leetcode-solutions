class Solution {
    public int maxProduct(int[] nums) {
        
        int product=1,max=Integer.MIN_VALUE,firstNeg=1;
        
        for(int i=0;i<nums.length;i++)
        {
            product=product*nums[i];
            if(product>=0)
            {
                max=Math.max(max,product);
                if(product==0)
                    product=firstNeg=1;
            }
            else
            {
                max=Math.max(max,product/firstNeg);
                
                if(firstNeg==1)
                    firstNeg=product;
            }
            
        }
    
        return max;
    }
}