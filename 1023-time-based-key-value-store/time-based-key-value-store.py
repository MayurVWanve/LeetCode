class TimeMap:

    def __init__(self):
        self.cache = {} #(key, timestamp -> val)
        self.lookup = defaultdict(list) #(key -> [Timestamps])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[(key, timestamp)] = value
        self.lookup[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # print(f'Key, timestamp : {key, timestamp}')

        if (key, timestamp) in self.cache:
            return self.cache[(key, timestamp)]

        if key not in self.lookup:
            # print(f'Key not in lookup')
            return ""

        heap = self.lookup[key]
        # print(f'Heap : {heap}')
        l,r = 0, len(heap) -1 

        if timestamp > heap[r]:
            return self.cache[(key, heap[r])]

        if timestamp < heap[l]:
            return ""

        while l<=r:
            m = (l+r)//2
            # print(l,r,m)

            if (l == r) or (l+1 == r):
                # print(f'This cond holds ')
                # print(f'{key, heap[l], self.cache[(key, heap[l])]}')
                return self.cache[(key, heap[l])]

            if (heap[m] > timestamp and heap[m-1] < timestamp):
                return self.cache[(key, heap[m-1])]
            
            if heap[m] < timestamp:
                l = m + 1
            
            else:
                r = m-1
        
        # return ""
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)