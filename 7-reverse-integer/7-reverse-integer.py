class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0:
            sign = 1
        else:
            sign = -1
        
        temp = abs(x)
        rev = 0
        while(temp != 0):
            rem = temp % 10
            rev = rev * 10 + rem
            if rev >= 2**31 - 1:
                return 0
            temp = temp // 10
        
        return sign*rev