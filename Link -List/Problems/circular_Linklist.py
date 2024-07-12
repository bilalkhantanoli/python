class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def inser_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        if itr is None:
            return
        llstr = ''
        while True:
            llstr += str(itr.data) + '-->'
            itr = itr.next
            if itr is None or itr == self.head:
                break
        llstr = llstr.rstrip('->')
        print(llstr)
    
    def getLength(self):
        count = 0
        iter = self.head
        while iter.next:
            count +=1
            iter = iter.next
        return count
    
    def cricluar_link_list(self):
        if self.head is None:
            print("Link list is empty")
            return
        if self.head.next is None:
            return
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = self.head
                break
            itr = itr.next
    
    


ll = LinkedList()
ll.inser_at_end(10)
ll.inser_at_end(20)
ll.inser_at_end(30)
ll.inser_at_end(40)
ll.inser_at_end(50)

ll.print()
ll.cricluar_link_list()
ll.print()
# print(ll.getLength())