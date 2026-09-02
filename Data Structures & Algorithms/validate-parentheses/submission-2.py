class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        
        stack = []
        pairs = {')':'(',']':'[','}':'{'}

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != pairs[c]:
                        return False
            
        return not stack

