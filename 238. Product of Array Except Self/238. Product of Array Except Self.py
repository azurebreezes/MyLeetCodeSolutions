class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans=[0]*n
        
        # left products
        l = [1]*(n+1)
        pre = 1
        for i in range(1,n+1):
            l[i] = pre*nums[i-1]
            pre = l[i]
        
        # right products
        r = [1]*(n+1)
        pre = 1
        for i in range(n-1,-1,-1):
            r[i] = pre*nums[i]
            pre = r[i]
        

        for i in range(n):
            ans[i] = l[i]*r[i+1]
        
        return ans