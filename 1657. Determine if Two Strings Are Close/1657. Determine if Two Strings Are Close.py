class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mp1 = {}
        feq1 = {}
        # Check characters
        for i in word1:
            if i in mp1:
                mp1[i] += 1
            else:
                mp1[i] = 1
        
        # Check frequency
        for i in mp1:
            if mp1[i] in feq1:
                feq1[mp1[i]] += 1
            else:
                feq1[mp1[i]] = 1

                
        mp2 = {}
        feq2 = {}
        for i in word2:
            if i not in mp1:
                return False
            if i in mp2:
                mp2[i] += 1
            else:
                mp2[i] = 1

        for i in mp2:
            if mp2[i] in feq2:
                feq2[mp2[i]] += 1
            else:
                feq2[mp2[i]] = 1
        return feq1 == feq2

            
        