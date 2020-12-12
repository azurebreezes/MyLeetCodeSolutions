class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        
        pre = nums[0]
        ctr=1

        for i in range(1, n):
            if nums[i]==pre:
                ctr+=1
            else:
                ctr=1
            pre = nums[i]
            if ctr==3:
                break
            if i==n-1:
                return n
            
        
        start = i
        for j in range(start, n):
            if nums[j]!=pre:
                nums[start]=nums[j]
                start+=1
                ctr=1
                pre = nums[j]
            else:
                if ctr==1:
                    nums[start]=nums[j]
                    start+=1
                    ctr+=1
                    pre = nums[j]  
        return(start)
            
        
