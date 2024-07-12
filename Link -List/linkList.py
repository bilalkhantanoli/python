class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def inser_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def inser_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.inser_at_end(data)
    
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
    def getLength(self):
        count = 0
        iter = self.head
        while iter.next:
            count +=1
            iter = iter.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >=self.getLength():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")
        if index == 0:
            self.inser_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1


if __name__ == '__main__':
    ll = LinkedList()
    # ll.inser_at_beginning(10)
    # ll.inser_at_beginning(20)
    # ll.inser_at_beginning(30)
    # ll.inser_at_end(40)
    # ll.inser_at_end(50)
    list = [1,2,3,4,5,6,7,8,8]
    ll.insert_values(list)
    ll.print()
    print(ll.getLength())
    ll.remove_at(3)
    ll.insert_at(3, "john")
    ll.print()
    print(ll.getLength())