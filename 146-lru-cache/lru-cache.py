
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
    def __init__(self, key=0, val=0):
        self.key = key
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


    def get(self, key: int) -> int:
        
        if key in self.lookup:

            node = self.lookup[key]
            p, n = node.prev, node.next
            p.next, n.prev = n, p
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node
            # print(" Get Worked Successfully")

            # c = self.dummy_head
            # while c:
            #     print(c.key)
            #     c = c.next

            return node.val
        else:
            # print(" Get Worked Successfully")
            return -1


    def put(self, key: int, value: int) -> None:

        if key in self.lookup:
            
            node = self.lookup[key]
            node.val = value
            p, n = node.prev, node.next
            p.next, n.prev = n, p
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node

        elif self.count == self.capacity:
            node = self.dummy_head.next
            nextN = node.next
            self.dummy_head.next, nextN.prev = nextN, self.dummy_head
            # print(f'Node to be deleted: {node.key} LookupTable: {self.lookup}')
            del(self.lookup[node.key])
            
            node = LinkedList(key, value)
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node
            self.lookup[key] = node
 
        else:
            node = LinkedList(key, value)
            last = self.dummy_tail.prev
            last.next, node.prev = node, last
            node.next, self.dummy_tail.prev = self.dummy_tail, node
            self.lookup[key] = node
            self.count+=1
        
        # print(" Put Worked Successfully")
        # c = self.dummy_head
        # while c:
        #     print(c.key)
        #     c = c.next



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)