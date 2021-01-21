class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = []
        mp = {}
        # Create mp to calculate and store the Euclidean distance
        for p in points:
            key = abs(p[0])**2 + abs(p[1])**2
            if key in mp:
                mp[key].append(p)
            else:
                mp[key] = [p]
        
    
        for i in sorted(mp):
            for j in mp[i]:
                # Append the closest points to ans
                ans.append(j)
                K -= 1
                if K == 0:
                    return ans
        
