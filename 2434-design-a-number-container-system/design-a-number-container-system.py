from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.numToIndex = {}  # Maps numbers to SortedSet of indices
        self.indexToNum = {}  # Maps indices to numbers
        
    def change(self, index: int, number: int) -> None:
        if index in self.indexToNum:
            old_number = self.indexToNum[index]
            if old_number in self.numToIndex:
                self.numToIndex[old_number].discard(index)
                if not self.numToIndex[old_number]:
                    del self.numToIndex[old_number]
        
        self.indexToNum[index] = number
        if number not in self.numToIndex:
            self.numToIndex[number] = SortedSet()
        self.numToIndex[number].add(index)
    
    def find(self, number: int) -> int:
        if number in self.numToIndex and self.numToIndex[number]:
            return self.numToIndex[number][0]  # Smallest index
        return -1