class Node:
    def __init__(self, data = 0, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class doublyLinkList:
    def __init__(self):
        self.head = None
    def insert_at_beggining(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node



    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beggining(data)
            return
        if self.head is None:
            self.head = Node(data, None, None)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def remove_at_beginning(self):
        if self.head is None:
            print("Link List is empty")
            return
        self.head = self.head.next
        self.head.prev = None
    
    def remove_at_end(self):
        if self.head is None:
            print("Link list is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    def remove_at(self, index):
        if self.head is None:
            print("Link List is empty")
            return
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.remove_at_beginning()
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            itr = itr.next
            count += 1

    def search(self, data):
        if self.head is None:
            print("Link List is empty")
            return
        itr = self.head
        while itr:
            if itr.data == data:
                return True
            itr = itr.next
        return False
        



    def get_length(self):
        count = 0
        if self.head is None:
            print("Link List is empty")
            return
        itr = self.head
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
    def display_reverse(self):
        if self.head is None:
            print("Link lIst is empty")
            return
        itr = self.head
        lstr = ""
        while itr.next:
            itr = itr.next
        while itr:
            lstr += str(itr.data) + "->"
            itr = itr.prev
        lstr = lstr.rstrip("->")
        print(lstr)
dl = doublyLinkList()
dl.insert_at_end(5)
dl.insert_at_end(6)
dl.insert_at_end(7)
dl.insert_at_beggining(1)
dl.display()
dl.insert_at(2,8)
dl.display()
# dl.remove_at_beginning()
# dl.display()
# dl.remove_at_end()
# dl.remove_at(2)
if dl.search(7):
        print("found")
else:
    print("not found")
dl.display()
dl.display_reverse()
print(dl.get_length())