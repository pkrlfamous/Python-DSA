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
            print("this is the value head", self.head.value, "node",node.next.value)
            yield node
            if self.head.prev == node:
                break
            node = node.next

    def creation(self,value):

        newNode = Node(value)

        newNode.next = newNode
        newNode.prev = newNode
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def insertion(self,value,position):
        newNode = Node(value)

        if self.head == None or self.length == 0:
            self.creation(value)
            return
        
        if self.length < position or position < -1:
            print("Index out of range")
            return
        
        if position == 0:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.head = newNode
            self.tail.next = newNode
            self.length += 1
            return
        
        if position == -1 or position == self.length:
            newNode.prev = self.tail
            newNode.next = self.tail.next

            self.tail.next = newNode
            self.tail = newNode
            self.head.prev = newNode
            self.length += 1
            return
        
        index = 0
        tempNode = self.head
        while index < position-1:
            tempNode = tempNode.next
            index += 1
        
        newNode.prev = tempNode
        newNode.next = tempNode.next

        tempNode.next.prev = newNode
        tempNode.next = newNode
        self.length += 1
        return


csll = CircularDoublyLinkedList()



csll.creation('a')
csll.insertion('hi there',0)
print('hre')
# print([node.value for node in csll])

csll.insertion('quick',2)
print([node.value for node in csll])

csll.insertion('gray',0)
csll.insertion('brown',-1)
csll.insertion('fox',-1)
csll.insertion('cat',2)
csll.insertion('over',csll.length)
csll.insertion('jumped',csll.length)
print([node.value for node in csll])