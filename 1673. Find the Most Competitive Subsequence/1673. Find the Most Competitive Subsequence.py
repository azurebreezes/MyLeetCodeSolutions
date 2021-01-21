class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        count = len(nums) - k
        
        for i in nums:
            while stack and i < stack[-1] and count > 0:
                stack.pop()
                count -= 1
            stack.append(i)

        return stack[:k]