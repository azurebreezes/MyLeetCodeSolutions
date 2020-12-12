class Solution:
    def reverse(self, x: int) -> int:
        isNeg=False
        if x < 0:
            x=-x
            isNeg=True
            
        ans=int(str(x)[::-1])
        if ans == 0 or ans >2**31-1 or ans <-2**31:
            return 0
        
        return ans if not isNeg else -ans
            