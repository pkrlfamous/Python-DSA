class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.next
    
    def creation(self,value):
        node = Node(value)

        if self.head == None:
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node

dll = DoublyLinkedList()

dll.creation(2)
print([node.value for node in dll])