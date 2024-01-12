class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        
    def pop(self):
        if len(self.items) != 0:
            self.items.pop()

    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        if target in self.items:
            return self.items[::-1].index(target)
        else:
            return -1