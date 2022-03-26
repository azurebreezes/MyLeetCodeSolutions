class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        # Sort the costs list base on the difference between aCost and bCost
        # Then costs[0] will have the minimum aCost, 
        # cost[n-1] will have the minimum bCost.
        costs.sort(key = lambda x : x[0] - x[1])            

        ans = 0
        # Each iteration, add both minimum aCost and bCost
        for i in range(n):
            ans += costs[i][0] + costs[n+i][1]
        return ans