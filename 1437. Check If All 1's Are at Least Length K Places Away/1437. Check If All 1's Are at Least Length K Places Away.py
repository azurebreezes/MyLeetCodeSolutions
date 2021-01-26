class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if pre == -1:
                    pre = i
                else:
                    if i - pre <= k:
                        return False
                pre = i

        return True
            
                
            