# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None 
                mergedLists.append(self.mergeLists(l1,l2))

            lists = mergedLists

        return lists[0]


            


    def mergeLists(self,l1,l2):
        l3 = h3 = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next

        l3.next = l1 if l1 else l2

        return h3.next

    


        