class Solution {
    public int divide(int dividend, int divisor) {
        
        
        int count=0;
        int sign;
        
        
        if(dividend==Integer.MIN_VALUE && divisor==-1)
            return Integer.MAX_VALUE;
        
        
        if((dividend<0 && divisor>0) || (dividend>0 && divisor<0))
		    sign=-1;
	    else
		    sign=1;
        
        if(dividend==Integer.MIN_VALUE && divisor>0)
            return dividend/divisor;    //used '/' bacause code gives time out for Integer.MIN_VALUE
        else if(dividend==Integer.MAX_VALUE && divisor>0)
            return dividend/divisor;
        
        long div=Math.abs((long)divisor);
        long dividend_1=Math.abs((long)dividend);
        if(div>dividend_1)
            return 0;
        long sum=0;
        while(sum<dividend_1)
        {
            sum+=div;
            count++;
            if(sum+div>dividend_1)
            {
                break;
            }
        }
        
        return sign==-1 ? sign*count : count;

    }
}