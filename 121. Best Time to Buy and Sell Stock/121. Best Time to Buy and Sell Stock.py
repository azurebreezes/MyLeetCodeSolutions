class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        ans = 0

        
        buy = prices[0]
        for i in prices:
            ans = max(i-buy,ans)
            buy = min(i,buy)
        return ans
        
        