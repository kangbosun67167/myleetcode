class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        # neg = 1
        mul = x
        if n < 0:
            # neg = -1
            mul = 1/x
            n = -n
        

        if n == 0:
            return 1

        out_ = 1
        
        while n:
            out_ = out_ * mul
            n -= 1
            
            if out_ < -2**31 or out_ > 2**31 -1 :
                return ValueError
        
        return out_
    
    def new_pow(self,x,n):
        ans=1
        if n==0:
                return 1
        if x==0:
            return 0
        if x==1:
            return 1
        if n<0:
            x=1/x
            n=-n
        ans=self.myPow(x,int(n/2))
        ans=ans*ans
        if (n%2==1):
            return ans*x
        return ans

print(Solution().new_pow(x=0.000017,n=214748364))