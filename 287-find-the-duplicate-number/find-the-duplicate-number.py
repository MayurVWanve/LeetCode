class LinkedList:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # search = {}
            
        # for i in range(len(nums)):
        #     node = LinkedList(i)
        #     search[i] = node
        # for i in range(len(nums)):
        #     node = search[i]
        #     node.next = search[nums[i]]

        # slow = fast =  search[0]
        
        # flag = True
        # while flag or fast != slow:
        #     flag = False
        #     slow = slow.next
        #     fast = fast.next.next
        
        # slow2 = search[0]

        # while slow2 != slow:
        #     slow2 = slow2.next
        #     slow= slow.next
        

        # return slow.val

        fast = slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0 
        while True:
            slow2 = nums[slow2]
            slow  = nums[slow]
            if slow2 == slow:
                break
        

        return slow

            
        
            
        

            

                



        