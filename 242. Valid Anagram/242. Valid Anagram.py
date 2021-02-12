class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        if len(s) != len(t):
            return False
        if not s or not t:
            return True
        
        for i in s:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        
        for j in t:
            if j in mp:
                mp[j] -= 1
            else:
                return False
        
        return (max(mp.values()) == 0)
        
        