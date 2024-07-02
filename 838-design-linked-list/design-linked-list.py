class LinkedList:
    def __init__(self, val=0):
        self.val = val 
        self.next= None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head, self.tail = LinkedList(), LinkedList()
        self.head.next, self.tail.prev = self.tail, self.head 
        self.count = 0

    def get(self, index: int) -> int:
        if index > self.count-1:
            return -1
        curr = self.head
        while index >= 0:
            curr = curr.next
            index-=1

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        node = LinkedList(val)
        curr = self.head.next
        self.head.next, node.prev = node, self.head
        node.next, curr.prev = curr, node
        self.count +=1   
        
        # print("AddAthead")
        # curr = self.head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next  

    def addAtTail(self, val: int) -> None:
        node = LinkedList(val)
        curr = self.tail.prev
        self.tail.prev, node.next = node, self.tail
        node.prev, curr.next = curr, node
        self.count +=1        
        # print(self.tail.prev.val)
        # print("AddAttail")
        # curr = self.head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return -1

        node = LinkedList(val)
        curr= self.head
        while index > 0:
            curr = curr.next
            index-=1
        
        nextN = curr.next
        curr.next, node.prev = node, curr
        node.next, nextN.prev = nextN, node
        self.count+=1

        # print("AddAtIndex")
        # curr = self.head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next


    def deleteAtIndex(self, index: int) -> None:
        if index > self.count -1:
            return -1
        
        curr = self.head

        while index > 0:
            curr = curr.next
            index-=1

        nextN = curr.next.next

        curr.next, nextN.prev = nextN, curr
        self.count-=1

        curr = self.head
        # print("DeleteAtIndex")
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)