class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        n = len(arr)
        ans=1
        while i < n:
            while ans < arr[i]:
                if k == 1:
                    return ans
                ans+=1
                k-=1
            if ans==arr[i]:
                ans+=1
                i+=1    
        return ans+k-1