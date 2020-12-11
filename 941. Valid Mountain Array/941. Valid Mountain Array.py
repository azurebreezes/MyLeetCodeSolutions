class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <3:
            return False
        pre = arr[0]
        
        # Up
        for i in range(1,n):
            if arr[i] > pre:
                pre = arr[i] 
            else:
                break
        if i == 1:
            return False
        
        # Down
        j=i
        for i in range(j, n):
            if arr[i] < pre:
                pre = arr[i]
            else:
                return False
        return True
    
                