class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        
        while high > low:
            tot = numbers[high] + numbers[low]
            if tot == target:
                return [low+1, high+1]
            elif tot > target:
                high-=1
            else:
                low+=1
        
        return [-1,-1]
        