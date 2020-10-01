class Solution {
    public int[] plusOne(int[] digits) {

        for(int i=digits.length-1;i>=0;i--)
        {
            if(digits[i]==9)
            {
                if(i==0)
                {
                    digits[i]=0;
                    digits=copy(digits);
                    break;
                }
                else
                {
                    digits[i]=0;
                }
            }
            else
            {
                digits[i]+=1;
                break;
            }
        }
        
        return digits;
}

private int[] copy(int[] digits){
    
    int newarray[]=new int[digits.length+1];
    
    newarray[0]=1;
    for(int i=1;i<digits.length;i++){
        newarray[i]=digits[i-1];
    }
    return newarray;
}
        
}      
        
        
        
        /*This approach wont work for 10+ digit arrays
        String dig = "";
        for(int num:digits){
            dig=dig+num;
        }
        long newno=Long.valueOf(dig)+1;
        String tempstr=String.valueOf(newno);
        int ans[]=new int[tempstr.length()];
        //System.out.println(newno);
        int i=0;
        while(newno!=0 && i<tempstr.length())
        {
            long rem=newno%10;
            ans[i++]=(int)rem;
            newno/=10;
        }
        
        
        int start=0,end=ans.length-1;
        while(start<end)
        {
            int temp=ans[start];
            ans[start]=ans[end];
            ans[end]=temp;
            start++;
            end--;
        }
        return ans;*/
        
        
