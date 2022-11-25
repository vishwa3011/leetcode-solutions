class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                s1 = s[i : j]
                s2 = s[i + 1 : j + 1]
                
                print(s1, s2)
                return s1 == s1[::-1] or s2 == s2[::-1]
            
            i += 1
            j -= 1
        
        return True
#             temp_list = list(s)
#             temp_list[i] = ""
#             new_s = "".join(temp_list)
            
#             if self.isPalindrome(new_s):
#                 return True
            
#             i += 1
            
#         return False
    
#     def isPalindrome(self, s):
        
#         i, j = 0, len(s)-1
        
#         while i < j:
#             if s[i] != "" and s[j] != "":
#                 if s[i] != s[j]:
#                     return False
#                 i += 1
#                 j -= 1
#             else:
#                 continue
    
#         return True