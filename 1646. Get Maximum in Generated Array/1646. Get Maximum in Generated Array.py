class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n==0:
            return 0
        n+=1
        #Initialize list
        arr = [0]*n
        arr[1] = 1
        # ans = 0
        
        # Update values in the list and then update ans
        for i in range(1,n):
            if i % 2 == 0:
                arr[i] = arr[i//2]
            else:
                arr[i] = arr[i//2] + arr[i//2+1]
            
            # ans = max(ans,arr[i])
        
        return max(arr)