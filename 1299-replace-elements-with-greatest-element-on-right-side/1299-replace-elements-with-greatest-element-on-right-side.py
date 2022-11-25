class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # if not arr:
        #     return []
        # else:
        #     greatest_elements = [-1]
            
        max_val = -1
        i = len(arr) - 1
        
        while i >= 0:
            arr[i], max_val = max_val, max(max_val, arr[i])
            i -= 1   
            #greatest_elements.append(max_val)
            
        return arr
        
#         j = 0
#         k = len(greatest_elements) - 1
        
#         while j <= k:
#             greatest_elements[j], greatest_elements[k] = greatest_elements[k], greatest_elements[j]
#             j += 1
#             k -= 1
        
#         return greatest_elements    