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
    
    def deletion(self, position):
        if self.head is None:
            print("Empty linked list.")
            return
        
        if position == 0:
            if self.length == 1 or self.head == self.head.next:
                self.head = None
                self.tail = None
                self.length = 0
            else:
                self.head = self.head.next
                self.tail.next = self.head
                self.length -= 1
            return
        
        if position > self.length - 1:
            print("Index out of range")
            return
        
        if position == -1 or position == self.length-1:
            if self.head == self.head.next or self.length == 1:
                self.head = None
                self.tail = None
                self.length = 0
            else:
                node = self.head
                while node.next != self.tail:
                    node = node.next
                
                node.next = self.head
                self.tail = node
                self.length -= 1
            return
        

        node = self.head
        for _ in range(position-1):
            node = node.next
        
        # this is dead block
        # ------
        if node.next == self.tail:
            node.next = node.next.next
            self.tail = node
            self.length -= 1
            return
        # ---------
        node.next = node.next.next
        self.length -= 1
        return
    
    def deleteAll(self):
        if self.length == 0:
            return
        
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
        print("The entire list has been deleted.")

    def searching(self,nodeValue):
        if self.head is None:
            print("List doesn't exist.")
            return

        node = self.head
        index = -1
        found = False
        while(node):
            index += 1
            if node.value == nodeValue:
                found = True
                break
            node = node.next
            if node == self.head:
                break
        
        if not found:
            print(f"{nodeValue} not found in the list.")
        else:
            print(f"{nodeValue} found in index {index}.")

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

csll.searching('a')
print(csll.tail.value)
csll.deletion(csll.length-1)
print(csll.tail.value)
print([node.value for node in csll])

# print([node.value for node in csll])
# csll.deletion(-1)
# print([node.value for node in csll])

csll.deleteAll()
print([node.value for node in csll])
