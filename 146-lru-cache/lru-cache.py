
# class LRUCache:
# Naive Solution
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.count = 0
#         self.stack = []
#         self.lookup = {}
    
#     def get(self, key: int) -> int:
#         if key in (self.lookup):
#             self.stack.remove(key)
#             self.stack.append(key)
#             return self.lookup[key]
#         else:
#             return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.lookup:
#             self.lookup[key] = value
#             self.stack.remove(key)
#             self.stack.append(key)

#         elif self.count == self.capacity:
#             ele = self.stack.pop(0)
#             del(self.lookup[ele])
#             self.stack.append(key)
#             self.lookup[key] = value


#         else:
#             self.count+=1
#             self.stack.append(key)
#             self.lookup[key] = value
            

class LinkedList:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None           


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.lookup = {}
        self.dummy_head, self.dummy_tail = LinkedList(), LinkedList()
        self.dummy_head.next, self.dummy_tail.prev = self.dummy_tail, self.dummy_head

    
    def deleteNode(self,key):
        curr = self.dummy_head
        while curr.next.val != key:
            curr = curr.next

        #Debug
        # c = self.dummy_head
        # print(f'Current : {curr.val}')
        # while c:
        #     print(c.val)
        #     c = c.next
        nextNode = curr.next.next
        curr.next, nextNode.prev = nextNode, curr
        return

    def get(self, key: int) -> int:
        
        if key in self.lookup:
            self.deleteNode(key)
            node = LinkedList(key)
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node
            # print(" Get Worked Successfully")

            # c = self.dummy_head
            # while c:
            #     print(c.val)
            #     c = c.next

            return self.lookup[key]
        else:
            # print(" Get Worked Successfully")
            return -1


    def put(self, key: int, value: int) -> None:

        if key in self.lookup:
            self.lookup[key] = value
            self.deleteNode(key)
            node = LinkedList(key)
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node

        elif self.count == self.capacity:
            node = self.dummy_head.next
            # print(f'Node to be deleted: {node.val} LookupTable: {self.lookup}')
            del(self.lookup[node.val])
            self.deleteNode(node.val)
            node = LinkedList(key)
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node
            self.lookup[key] = value
 
        else:
            node = LinkedList(key)
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node
            self.lookup[key] = value
            self.count+=1
        
        # print(" Put Worked Successfully")



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)