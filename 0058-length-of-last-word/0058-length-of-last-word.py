class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        list_strings = s.strip().split(" ")
        print(list_strings)
        
        return len(list_strings[-1])