class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head

        # print('here')
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
    

    def insertion(self,value, position):
        newNode = Node(value)

        if self.length == 0 or self.head == None or self.tail == None:
            self.creation(value)
            return
        
        if position == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
            self.length += 1
            return
        
        if position == -1 or position == self.length:
            newNode.next = self.head
            self.tail.next =  newNode
            self.tail = newNode
            self.length += 1
            return
        
        if position > self.length:
            print('Index out of range')
            return
        
        index = 0
        tempNode = self.head
        while(index < position-1):
            # print('this is index',index)
            tempNode = tempNode.next
            index += 1
        
        newNode.next = tempNode.next
        tempNode.next = newNode
        self.length += 1
    
    def traverse(self):
        node = self.head
        list = []
        length = 0
        while(node):
            length += 1
            list.append(node.value)
            if self.head == node.next:
                break
            node = node.next
        print(list)
        print('length traverse', length)


csll = CircularSinglyLinkedList()
csll.creation('a')
csll.insertion('hi there',0)
csll.insertion('quick',2)
csll.insertion('gray',0)
csll.insertion('brown',-1)
csll.insertion('fox',-1)
csll.insertion('cat',2)
csll.insertion('over',csll.length)
csll.insertion('jumped',csll.length)
print([node.value for node in csll])

