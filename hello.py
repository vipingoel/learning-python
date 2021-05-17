class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0 :
            x = -x
            is_neg = True
            
        print(x)
        res = 0
        while x:
            dig = x % 10
            res = res*10 + dig
            x = int(x/10)

        print(res)
        if is_neg:
            res = -res
        
        print(res)
        
        if (res > (2**31) - 1) or (res < -(2**31 - 1)):
            print("in")
            return 0

        return res
    
print(Solution().reverse(-123))