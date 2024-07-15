class stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
print(s.peek())
print(s.isEmpty())
print(s.size())