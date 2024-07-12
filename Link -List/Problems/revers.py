class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class linkList:
    def __init__(self):
        self.head = None

    def getLength(self):
        if self.head is None:
            print("Link List is empty")
            return
        itr = self.head
        count = 0
        while itr:
            count +=1
            itr = itr.next
        return count
    def display(self):
        if self.head is None:
            print("Link List is empty")
            return
        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.data) + "->"
            itr = itr.next
        lstr = lstr.rstrip("->")
        print(lstr)

        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def reverse(self):
        if self.head is None:
            print("Link list is empty")
            return
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def rotate(self, k):
        if self.head is None:
            print("Link list is empyt")
            return
        if k > self.getLength():
            print(f"{k} is greater than link list length")
            return
        if k == 0 or k < 0:
            print(f"{k} is not valid")
            return
        current = self.head
        for i in range(k -1):
            current = current.next
        kth = current        
        while current.next:
            current = current.next
        current.next = self.head
        self.head = kth.next
        kth.next = None

ll = linkList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.display()
# ll.reverse()
ll.rotate(2)
ll.display()