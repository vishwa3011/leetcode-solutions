class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {')' : '(', '}' : '{', ']' : '['}
        
        open_b = ['(', '[','{']
        
        stack = []
        
        for i in range(len(s)):
            if s[i] in open_b:
                stack.append(s[i])
            elif stack and hashmap[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return True if not stack else False
        