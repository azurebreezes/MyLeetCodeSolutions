class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        pre_c = -len(s)
        start = 0
        for i in range(len(s)):
            if s[i] == c:
                for j in range(start, i+1):
                    ans.append(min(i-j, j-pre_c))
                start = i+1
                pre_c = i

        if s[-1] != c:
            for k in range(start, len(s)):
                ans.append(k - pre_c)
        return ans
        