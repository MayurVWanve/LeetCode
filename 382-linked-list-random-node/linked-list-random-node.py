# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.lookup = {}
        self.n = 0
        while head:
            self.n+=1
            self.lookup[self.n] = head.val
            head = head.next
        

    def getRandom(self) -> int:
        number = random.randint(1,self.n)
        return self.lookup[number]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()