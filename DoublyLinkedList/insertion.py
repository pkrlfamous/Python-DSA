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
        while node:
            yield node
            node = node.next

    def creation(self,value):

        node = Node(value)
        self.head = node
        self.tail = node

    def insertIntoList(self, value, position):
        node = Node(value)

        if self.head is None:
            print("The node cannot be inserted.")
            return
        
        if position == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif position == -1:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            index = 0
            tempNode = self.head
            while tempNode and index < position - 1:
                tempNode = tempNode.next
                index += 1
            if tempNode == self.tail or tempNode is None:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                node.next = tempNode.next
                node.prev = tempNode
                tempNode.next.prev = node
                tempNode.next = node


dll = DoublyLinkedList()
dll.creation(0)
# print([node.value for node in dll])

dll.insertIntoList(1,1)
dll.insertIntoList(2,2)

print([node.value for node in dll])


