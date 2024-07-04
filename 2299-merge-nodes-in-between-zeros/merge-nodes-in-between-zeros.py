# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l = ListNode()
        curr, temp = head.next, 0

        while curr:
            if curr.val == 0:
                node = ListNode(temp)
                l.next = node
                l = l.next
                temp = 0
            
            else:
                temp+=curr.val
            
            curr = curr.next
            
        return dummy.next
        