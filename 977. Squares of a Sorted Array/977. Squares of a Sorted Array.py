#Approach 1 calculate and sort
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        return sorted(nums)

#Approach 2 two pointers