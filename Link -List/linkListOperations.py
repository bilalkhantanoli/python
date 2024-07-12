class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self, head = None):
        self.head = head
    
    def insert_at_beggining(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_index(self, prev, data):
        if self.head is None:
            print("link lis is empty")
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            if itr.data == prev:
                node = Node(data)
                node.next = itr.next
                itr.next = node
            itr = itr.next
        
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
    
    def delete_at_beggining(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next
    
    def delete_at_end(self):
        if self.head is None:
            print("Linked list empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None
        
    def delete_at_index(self, idx):
        if idx > self.get_length():
            print("Link list out of range")
            return

        if idx == 0:
            self.delete_at_beggining()
            return

        count = 0
        itr = self.head 
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def get_length(self):
        if self.head is None:
            print("Link List is empty")
            return
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
        
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.data) + "->"
            itr = itr.next
        lstr = lstr.rstrip("->")
        print(lstr)

linklist = LinkList()
linklist.insert_at_beggining(10)
linklist.insert_at_beggining(20)
linklist.insert_at_beggining(30)
linklist.insert_at_end('end')
linklist.insert_at_index(30, "hello")
# linklist.delete_at_beggining()
# linklist.delete_at_end()
linklist.delete_at_index(3)
print(linklist.get_length())


linklist.display()