class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) < 1):
            return 
        def expandAroundCenter(s, left, right):
            L = left
            R = right

            while (L >= 0 and R < len(s) and s[L] == s[R]):
                L-=1
                R+=1

            return R - L - 1

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i+1)
            len0 = max(len1, len2)

            if (len0 > (end - start)):
                start = i - (len0 - 1) // 2
                end = i + len0 // 2

        return s[start:end+1]
    
   
            
            
        