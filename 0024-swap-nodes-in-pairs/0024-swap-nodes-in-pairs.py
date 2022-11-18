# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr and curr.next:
            nextPair = curr.next.next
            second = curr.next
            
            ## reverse the pair
            second.next = curr
            curr.next = nextPair
            prev.next = second
            
            ## updating
            prev = curr
            curr = curr.next
        
        return dummy.next
            
#         if not head or not head.next:
#             return head
        
#         first = head
#         second = head.next
        
        
#         ## Swapping
#         first.next = self.swapPairs(second.next)
#         second.next = first
        
#         return second_node

