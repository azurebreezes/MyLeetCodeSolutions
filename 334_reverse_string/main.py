class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # Create two pointers, swap the values between the s[ptr]
        ptr1 = 0
        ptr2 = len(s)-1
        
        while ptr1 < ptr2:
            temp = s[ptr1]
            
            s[ptr1] = s[ptr2]
            s[ptr2] = temp
            
            ptr1 += 1
            ptr2 -= 1