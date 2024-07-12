class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val)

    def merge_nodes_between(self):
        if self.head is None:
            return
        dummy = Node()
        dummy.next = self.head
        prev = dummy
        current = self.head
        sum_ = 0
        while current:
            if current.val == 0:
                if sum_ != 0:
                    prev.next = Node(sum_)
                    prev = prev.next
                    sum_ = 0
            else:
                sum_ += current.val
            current = current.next
        if dummy.next and dummy.next.val == 0:
            self.head = dummy.next.next
        else:
            self.head = dummy.next

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.val) + "->"
            itr = itr.next
        lstr = lstr.rstrip("->")
        print(lstr)

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
    
    def delete_N_nodes_after_M_nodes(self, n, m):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.getLength() < m:
            print("Linked List length is less than M")
            return
        itr = self.head
        while itr:
            for i in range(m-1):
                itr = itr.next
            current = itr
            for i in range(n):
                current = current.next
            itr.next = current.next
            itr = itr.next

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_end(6)
ll.insert_at_end(7)
ll.insert_at_end(8)
ll.insert_at_end(9)
ll.insert_at_end(10)
ll.display()
# ll.merge_nodes_between()
ll.delete_N_nodes_after_M_nodes(2, 3)
ll.display()
