class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        mp={}
        i=0
        for j in range(len(s)):
            if s[j] in mp:
                i=max(mp[s[j]]+1,i)
            ans=max(ans, j-i+1)
            mp[s[j]]=j
        return ans