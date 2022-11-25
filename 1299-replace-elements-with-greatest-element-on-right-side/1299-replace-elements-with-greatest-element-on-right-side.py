class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if not arr:
            return []
        else:
            greatest_elements = [-1]
            
        max_val = 0
        i = len(arr) - 1
        
        while i > 0:
            if arr[i] > max_val:
                max_val = arr[i]
            
            i -= 1   
            greatest_elements.append(max_val)
        
        return list(reversed(greatest_elements))            