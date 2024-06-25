# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        aux, h1, h2 = 0, l1,l2 
        h3 = dummy = ListNode()

        while h1 and h2:
            new_val = h1.val + h2.val + aux
            if new_val // 10 != 0:
                aux = new_val//10
                new_val = new_val%10
            else:
                aux = 0

            h3.next = ListNode(val = new_val)
            h1 = h1.next
            h2 = h2.next
            h3 = h3.next
        
        while h1:
            new_val = h1.val + aux
            if new_val // 10 != 0:
                aux = new_val//10
                new_val = new_val%10
            else:
                aux = 0

            h3.next = ListNode(val = new_val)
            h1 = h1.next
            h3 = h3.next

        while h2:
            new_val = h2.val + aux
            if new_val // 10 != 0:
                aux = new_val//10
                new_val = new_val%10
            else:
                aux = 0

            h3.next = ListNode(val = new_val)
            h2 = h2.next
            h3 = h3.next
        
        if aux != 0:
            h3.next = ListNode(val = aux)
            h3 = h3.next

            
        return dummy.next