'''
In this chapter we learn the diffrence between lined list and arrays .
You can find the diffrence in detail in the txt file.
In this file wewill learn how tocreatelinkedlist and assign some methods like
*Insert at the end.
*Insert at the beginning.
*Insert more than one value.

P.S ==> There will be another version of code to cover more complicated methods.
'''
class Node: # Every element in linkedlist is a node and it contains the data and the location of next value
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_the_beginning(self, data): #Insert at the begnning means that the node equal to the head
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("The list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '==>'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data): #Insert at the end means that the last value has no next or next=None
        if self.head is None:
            node = Node(data, None)
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for elem in data_list:
            self.insert_at_end(elem)
        
        
        # V2 Methods
    def get_length(self):
        count = 0

        itr = self.head

        while itr.next:
            itr = itr.next
            count += 1
        return count
    
    def remove(self, index):
        if index < 0 or index >= self.get_length():
            return Exception("Nota valid index")

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
        if index < 0 or index >= self.get_length():
            return Exception('Not a valid index')

        if index == 0:
            node = Node(data, self.head)  
            self.head = node

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_by_data(self, data):
        if self.head is None:
            return Exception("No element in the list")

        if data == self.head.data:
            self.head = self.head.next

        itr = self.head

        while itr.next:
            if data == itr.next.data:
                itr.next = itr.next.next
                break
            itr = itr.next
    def add_after(self, data, data_after):
        if self.head is None:
            return Exception("No element in the list")

        if data_after == self.head.data:
            self.head.next = Node(data, self.head.next)

        itr = self.head

        while itr:
            if data_after == itr.data:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next

lst = LinkedList()
lst.insert_at_the_beginning(50)
lst.insert_at_the_beginning(60)
lst.insert_at_end(100)
lst.insert_values([50, 100, 65])
print(lst.get_length())
lst.remove(2)
lst.print()
lst.remove_by_data(65)
lst.add_after(88, 60)
lst.print()