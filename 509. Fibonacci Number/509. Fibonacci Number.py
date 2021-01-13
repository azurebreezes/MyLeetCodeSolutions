class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n <=2:
            return 1
        
        pre1=1
        pre2=1
        ans = 0
        for i in range(3,n+1):
            ans = pre1+pre2
            pre1=pre2
            pre2=ans
        return ans