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

    def middle(self):
        if self.head is None:
            print("Link List is empty")
            return
        length = self.getLength()
        itr = self.head
        for i in range(length//2):
            itr = itr.next
        print(itr.data)

    def delete_middle(self):
        if self.head is None:
            print("Link list is empty")
            return
        length = self.getLength()
        if length == 1:
            self.head = None
            return
        itr = self.head
        for i in range(length//2 - 1):
            itr = itr.next
        
        itr.next = itr.next.next
        
    def kth_node_from_end(self, k):
        if self.head is None:
            print("Link List is empty")
            return
        itr = self.head
        length = self.getLength()
        for i in range(length - k):
            itr = itr.next
        print(itr.data)
    
    #delete-last-occurrence-of-an-item-from-linked-list
    def delete_last_occurrence(self, data):
        if self.head is None:
            print("Link list is empty")
            return
        
        itr = self.head
        occurence = None
        occurence_prev = None
        prev = None
        while itr:
            if itr.data == data:
                occurence = itr
                occurence_prev = prev
            prev = itr
            itr = itr.next
        if occurence:
            if occurence == self.head:
                self.head = self.head.next
            elif occurence_prev.next:
                occurence.data = occurence.next.data
                occurence.next = occurence.next.next
            else:
                occurence_prev.next = None

    
    def remove_sorted(self):
        if self.head is None:
            print("Link List is empty")
            return
        
        itr = self.head
        while itr and itr.next:
            if itr.next.data == itr.data:
                itr.next = itr.next.next
            else:
                itr = itr.next

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def find_maximum_and_minimum_nodes_between_betweeen_critical_nodes(self):
        if not self.head or not self.head.next or not self.head.next.next:
            return [-1, -1]

        critical_positions = []
        current = self.head
        index = 1
        
        while current.next and current.next.next:
            if (current.next.data > current.data and current.next.data > current.next.next.data) or \
               (current.next.data < current.data and current.next.data < current.next.next.data):
                critical_positions.append(index)
            current = current.next
            index += 1

        if len(critical_positions) < 2:
            return [-1, -1]

        min_distance = float('inf')
        max_distance = critical_positions[-1] - critical_positions[0]

        for i in range(1, len(critical_positions)):
            min_distance = min(min_distance, critical_positions[i] - critical_positions[i - 1])

        return [min_distance, max_distance]     



ll = linkList()
ll.insert_at_end(5)
ll.insert_at_end(3)
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(5)
ll.insert_at_end(1)
ll.insert_at_end(2)
# ll.insert_at_end(1)
# ll.insert_at_end(3)
# ll.insert_at_end(2)
# ll.insert_at_end(2)
# ll.insert_at_end(3)
# ll.insert_at_end(2)
# ll.insert_at_end(2)
# ll.insert_at_end(2)
# ll.insert_at_end(7)
ll.display()
print(ll.find_maximum_and_minimum_nodes_between_betweeen_critical_nodes())
# ll.middle()
# ll.delete_middle()
# ll.kth_node_from_end(4)
# ll.delete_last_occurrence(20)
# ll.remove_sorted()
# ll.display()