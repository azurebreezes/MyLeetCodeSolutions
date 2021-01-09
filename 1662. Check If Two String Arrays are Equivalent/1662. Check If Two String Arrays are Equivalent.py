class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        s2 = ""
        for item in word1:
            s1+=item
        for item in word2:
            s2+=item

        return s1==s2