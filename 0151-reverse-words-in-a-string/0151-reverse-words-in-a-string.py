class Solution:
    def reverseWords(self, s: str) -> str:
        
        stack = []
        result = ""
        
        for word in s.split(" "):
            if word != '':
                stack.append(word)
                
        while stack:
            result += stack.pop() + " "
        
        return result.rstrip()