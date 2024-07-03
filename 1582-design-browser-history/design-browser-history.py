class LinkedList:
    def __init__(self, val=''):
        self.val = val
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = LinkedList(homepage)
        self.tail = LinkedList()
        self.head.next, self.tail.prev = self.tail, self.head
        self.count_front = 0
        self.count_back = 0
        self.curr = self.head

    def visit(self, url: str) -> None:
        node = LinkedList(url)
        self.curr.next, node.prev = node, self.curr
        node.next, self.tail.prev = self.tail, node
        self.curr = self.curr.next
        self.count_back+=1
        self.count_front = 0
        
        print("Visit: ")
        new = self.head
        while new:
            print(new.val)
            new = new.next
        
        print("Curr: ", self.curr.val)
        

    def back(self, steps: int) -> str:
        print("Count_front, Count_back", self.count_front, self.count_back)
        if steps > self.count_back:
            self.curr = self.head
            self.count_front+=self.count_back
            self.count_back = 0
            
            
        else:
            while steps!=0:
                self.curr = self.curr.prev
                self.count_back-=1
                self.count_front +=1
                steps-=1

        print("Back: ")
        new = self.head
        while new:
            print(new.val)
            new = new.next
        print("Curr: ", self.curr.val)

        return self.curr.val

    def forward(self, steps: int) -> str:
        print("Count_front, Count_back", self.count_front, self.count_back)
        if steps > self.count_front:
            self.curr = self.tail.prev
            self.count_back += self.count_front
            self.count_front = 0
            
        
        else:
            while steps!=0:
                self.curr = self.curr.next
                self.count_front-=1
                self.count_back+=1
                steps-=1

        print("Forward: ")
        new = self.head
        while new:
            print(new.val)
            new = new.next
        print("Curr: ", self.curr.val)

        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)