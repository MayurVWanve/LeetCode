
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.stack = []
        self.lookup = {}
    
    def get(self, key: int) -> int:
        if key in (self.lookup):
            self.stack.remove(key)
            self.stack.append(key)
            return self.lookup[key]
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key] = value
            self.stack.remove(key)
            self.stack.append(key)

        elif self.count == self.capacity:
            ele = self.stack.pop(0)
            del(self.lookup[ele])
            self.stack.append(key)
            self.lookup[key] = value


        else:
            self.count+=1
            self.stack.append(key)
            self.lookup[key] = value
            
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)