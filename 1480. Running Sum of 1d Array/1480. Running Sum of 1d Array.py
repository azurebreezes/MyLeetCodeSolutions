class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = 0
        for i in nums:
            pre += i
            yield pre
            