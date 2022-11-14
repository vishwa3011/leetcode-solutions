# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        prev = ListNode(0)
        prev.next = curr
        
        length = self.get_length(curr)
        remove_index = length - n + 1
        
        if remove_index == 1: #beginning of the linkedlist
            temp = head
            head = head.next
        else:
            i = 0
            while i < remove_index - 1:
                i += 1
                prev = curr
                curr = curr.next

            #print(length, remove_index, prev.val, curr.val)
            prev.next = curr.next
            curr = None
        
        return head
        
        
    def get_length(self, node):
        n = 0
        while node:
            n += 1
            node = node.next
        return n