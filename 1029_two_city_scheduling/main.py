class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        # Sort the costs list base on the difference between aCost and bCost
        costs.sort(key = lambda x : x[0] - x[1])            

        ans = 0
        # From i in range 0 to n, the costs[i] will have a lower aCost. 
        # For range n + i to 2n, the costs[n+i] will have a lower bCost.
        # For each iteration, add the lower aCost and bCost from the list
        for i in range(n):
            ans += costs[i][0] + costs[n+i][1]
        return ans