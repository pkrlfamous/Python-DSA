class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:

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
        newNode.next = newNode

        self.head = newNode
        self.tail = newNode
        self.length = 1


csll = CircularSinglyLinkedList()


csll.creation('a')

print(csll.head.value)
print(csll.tail.value)
print(csll.length)

print([node.value for node in csll])