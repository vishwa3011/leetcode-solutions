class Solution {
    public boolean isPalindrome(int x) {
        
        
        int temp=x;int rev=0;
        while(temp>=1)
        {
            int rem=temp%10;
            rev=rev*10+rem;
            temp/=10;
        }
        return rev==x;
    }
}