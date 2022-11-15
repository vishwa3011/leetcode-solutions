class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0
        j = 0
        index = float('inf')
        
        if len(needle) > len(haystack):
            return -1
        c = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                index = min(index, i)
                i += 1
                j += 1
                c += 1
            else:
                j = 0
                i = i - c + 1
                c = 0
                index = float('inf')
        
        if index == float('inf') or j != len(needle):
            return -1
        
        return index