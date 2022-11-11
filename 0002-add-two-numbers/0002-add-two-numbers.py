# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = l1
        len1 = 0
        while temp1:
            len1 += 1
            temp1 = temp1.next
            
        temp2 = l2
        len2 = 0
        while temp2:
            len2 += 1
            temp2 = temp2.next
        
        tail1 = l1
        tail2 = l2
        #print(len1, len2)
        
        if len1 > len2:
            
            while tail2.next:
                tail2 = tail2.next
                
            for i in range(len1 - len2):
                tail2.next = ListNode(0)
                tail2 = tail2.next
                
        elif len2 > len1:
            
            while tail1.next:
                tail1 = tail1.next
                
            for i in range(len2 - len1):
                tail1.next = ListNode(0)
                tail1 = tail1.next
                
        #print(l1, l2)
        
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
            