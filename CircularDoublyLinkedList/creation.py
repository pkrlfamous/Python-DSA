class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
    

class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head
        while(node):
            yield node
            if self.head == node.next:
                break
            node = node.next
    
    def creation(self,value):

        newNode = Node(value)

        self.head = newNode
        newNode.next = self.head
        newNode.prev = self.head
        self.tail = newNode

cdll = CircularDoublyLinkedList()
cdll.creation(4)

print([node.value for node in cdll])