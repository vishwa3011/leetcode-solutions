# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        output = ListNode()
        tail1 = output
        
        greaternodes = ListNode()
        tail2 = greaternodes
        
        curr = head
        
        while curr:
            if curr.val < x:
                tail1.next = curr
                tail1 = tail1.next
            else:
                tail2.next = curr
                tail2 = tail2.next
            curr = curr.next
        
        tail2.next = None
        tail1.next = greaternodes.next
        
        return output.next