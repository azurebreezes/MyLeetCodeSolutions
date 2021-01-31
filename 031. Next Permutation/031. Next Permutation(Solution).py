class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
        def reverse(arr, start):
            i = start
            j = len(nums) - 1
            while(i < j):
                swap(arr, i, j)
                i += 1
                j -= 1

            
        i = len(nums) - 2
        
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
            
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            swap(nums, i, j)
            
        reverse(nums, i+1)
            
        