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

lst = LinkedList()
lst.insert_at_the_beginning(50)
lst.insert_at_the_beginning(60)
lst.insert_at_end(100)
lst.insert_values([50, 100, 65])

lst.print()