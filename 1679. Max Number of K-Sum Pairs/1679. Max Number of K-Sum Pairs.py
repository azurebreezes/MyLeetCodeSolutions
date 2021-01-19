class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        ans = 0
        
        n = len(nums)
        
        lo, hi = 0, n-1
        
        while hi > lo:
            
            sum = nums[lo] + nums[hi]
            
            if sum == k:
                ans += 1
                lo += 1
                hi -= 1
            elif sum > k:
                hi -= 1
            else:
                lo += 1
        
        return ans
                
            