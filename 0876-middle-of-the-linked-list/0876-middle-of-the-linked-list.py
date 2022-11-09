# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
        
        middle = length//2
        
        mid_pointer = head
        i = -1
        while head:
            i += 1
            
            if i == middle:
                mid_pointer = head
                
            head = head.next
        
        return mid_pointer