class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ']':'[',
             ')':'(',
             '}':'{',
             }
        
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            elif len(stack) > 0:
                temp = stack.pop()
                if temp == mp[i]:
                    continue
                else:
                    return False
            elif len(stack) == 0:
                return False
        if len(stack) == 0:
            return True
        return False