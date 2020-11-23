class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        neg=False
        if x<0:
            neg=True
            x=x*-1
        while x != 0:
            rem = x%10
            rev = rev*10 + rem
            if rev > 2**31 - 1 or rev < -2**31:
                return 0
            x=x//10
        if neg == True:
            rev = rev*-1
        return rev