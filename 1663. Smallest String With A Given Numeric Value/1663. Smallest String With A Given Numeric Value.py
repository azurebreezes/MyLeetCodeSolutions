class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        # keep space for a's
        k -= n
        
        # string of z's
        z = "z"* (k // 25)
        
        # character other than a or z
        mid = ""
        if k % 25 != 0:
            mid = chr(97 + k % 25)
        
        # string of a's
        a = "a" * (n - len(z) - len(mid))
        
        # concatenate strings and return
        return a + mid + z
        
        