# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        if not curr:
            return False
        slow = curr
        fast = curr.next
        
        while slow != fast:
            
            if not fast or not fast.next:
                return False
                
            slow = slow.next
            fast = fast.next.next
            
        
        return True