class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s) - 1
        
        # Strip, skip the leading and trailing spaces
        while l <= r and s[l] == ' ':
            l += 1
        while l <= r and s[r] == ' ':
            r -= 1
            
        # Find each word, and append it to the left of the deque
        # Which will end up a reversed order of words
        d, word = collections.deque(), []
        while l <= r:
            if s[l] == ' ' and word:
                d.appendleft(''.join(word))
                word.clear()
            elif s[l] != ' ':
                word.append(s[l])
            l += 1
        d.appendleft(''.join(word))
        return ' '.join(d)