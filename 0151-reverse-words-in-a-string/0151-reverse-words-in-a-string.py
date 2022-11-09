class Solution:
    def reverseWords(self, s: str) -> str:
        
        stack = []
        result = ""
        
        for word in s.split(" "):
            if word != '':
                stack.append(word)
        
        print(stack)
        
        while stack:
            result += stack.pop() + " "
        
        return result.rstrip()
    
#         new_str = ""
#         reverse_str = ""
#         s = s.strip()
        
#         for i in range(len(s)-1,-1,-1):
            
#             if s[i] == ' ':
#                 reverse_str += self.reverse(new_str)
#                 new_str = ""
#                 print(reverse_str)
                
#             new_str += s[i]
        
#         reverse_str += self.reverse(new_str)
        
#         return reverse_str
        
#     def reverse(self, word_str):
#         i, j = 0, len(word_str) - 1
        
#         word = list(word_str)
        
#         while i < j:
#             word[i], word[j] = word[j], word[i]
#             i += 1
#             j -= 1
        
#         return ''.join(word)