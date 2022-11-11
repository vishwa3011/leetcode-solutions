# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        len1 = self.get_length(l1)
        len2 = self.get_length(l2)
        
        if len1 > len2:
            l2 = self.adjust_size(len1, len2, l2)    
        elif len2 > len1:
            l1 = self.adjust_size(len2, len1, l1)
                        
        sum_list = ListNode()
        tail = sum_list
        carry = 0
        
        while l1 and l2:
            
            sum_val = l1.val + l2.val + carry
            carry = 0
            if sum_val >= 10:
                sum_val %= 10
                carry = 1
                
            tail.next = ListNode(sum_val)
            
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        if carry != 0:
            tail.next = ListNode(carry)
            
        return sum_list.next
    
    
    def get_length(self, node):
        temp = node
        n = 0
        while temp:
            n += 1
            temp = temp.next
            
        return n
    
    def adjust_size(self, big, small, node):
        
        tail = node
        while tail.next:
            tail = tail.next
                
        for i in range(big - small):
            tail.next = ListNode(0)
            tail = tail.next
        
        return node