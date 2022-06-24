class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        g -> len(g) is number of children
             g[i] is the greed factor of that respective children
        s -> len(s) is number of cookies
             s[i] is size of a cookie
        '''
        
        content = 0
        n_child = len(g)
        n_cookie = len(s)
        i = 0
        
        while n_cookie != 0 and n_child != 0:
            max_c = max(s)
            max_g = max(g)
            if max_g <= max_c:
                content += 1 # assigned this cookie to kid
                s.remove(max_c) # removed the maximum element
                g.remove(max_g)
    
                if s != None and g != None:
                    n_cookie = len(s)
                    n_child = len(g)
                else:
                    break
            else:
                if g != None:
                    g.remove(max_g)
                    n_child = len(g)
                else:
                    break
                
        return content
                    
#         # Brute force
        
#         for i in range(n_cookie):
#             content_c = 0
#             for j in range(n_child):
#                 if s[i] >= g[j]:
#                     content_c += 1
            
#             if content_c <= n_cookie:
#                 content = max(content, content_c)
#             else:
#                 content = n_cookie
                    
#         return content