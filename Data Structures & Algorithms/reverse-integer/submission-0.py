class Solution:
    def reverse(self, x: int) -> int:
        if x <0 and x > -2**31:
            x = str(x)[1:]
            return int(x[::-1])*-1
        elif x >= 0 and int(str(x)[::-1]) < (2**31)-1:
            return int(str(x)[::-1])
        else:
            return 0
        
        