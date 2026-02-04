import time
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
        if not node:
            print("empty list")
            return
        
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

    def forwardTraverse(self):
        if not self.head:
            return
        
        node = self.head
        result = []
        # print('traverse',self.head.value, self.tail.value, node.value, )
        while True:
            result.append(node.value)
            # print('node.next',node.value, node.next, node.next.value, 'self head', self.head.value, self.head)
            if node.next == self.head:
                break
            # print('before assign',node)
            node = node.next
            # print('after assign',node)
            # print('here')
            print(result)

    def backWardTraverse(self):
        if not self.tail:
            return
        
        node = self.tail
        result = []
        while True:
            result.append(node.value)
            if node.prev == self.tail:
                break
            node = node.prev
        print('reversetraverse',result)
    

    def deletion(self,position):
        
        if not self.head:
            print("empty list")
            return
        
        if position == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            self.length -= 1
            return
        

        if position == -1:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev= None
                self.head = None
                self.tail = None

            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            self.length -= 1
            return
        
        index = 0
        tempNode = self.head

        # # traverse to the item to be deleted.
        # while index < position:
        #     tempNode = tempNode.next
        #     print('tempnode',tempNode.value)
        #     if tempNode.next == self.tail:
        #         print("index out of range")
        #         break
        #     index += 1
        
        # if tempNode.next == self.tail:
        #     self.tail = self.tail.prev
        #     self.tail.next = self.head
        #     self.head.prev = self.tail
        #     self.length -= 1
        #     return
        
        # tempNode.prev.next = tempNode.next
        # tempNode.next.prev = tempNode.prev
        # self.length -= 1

        # traverse to just 1 below the item to be deleted.
        index = 0
        tempNode = self.head
        print('position',position)
        while index < position - 1:
            tempNode = tempNode.next
            index += 1

            if tempNode.next == self.head:
                print("No node exist in provided position")
                return

        if tempNode.next == self.tail:
            tempNode.next = self.tail.next
            self.tail = tempNode
            self.head.prev = tempNode
            self.length -= 1
            return
        
        tempNode.next = tempNode.next.next
        tempNode.next.prev = tempNode
        self.length -= 1

    # def searching(self,value):
    #     if not self.head:
    #         print('list does not exist')
    #         return
        
    #     node = self.head
    #     index = 0
    #     found = False
    #     while True:
    #         index += 1
    #         if node.value == value:
    #             found = True
    #             break

    #         if node.next == self.head:
    #             break
    #         node = node.next
        
    #     if not found:
    #         print('value does not exist')
    #         return
        
    #     print(f"{value} found in position {index}")

    def searching(self, value):
        if not self.head:
            print('List does not exist')
            return
        
        node = self.head
        index = 0
        
        while True:
            if node.value == value:
                print(f"{value} found in index {index}")
                return # Exit immediately when found
            
            if node.next == self.head:
                break # We've gone full circle
            
            node = node.next
            index += 1
        
        print(f'{value} does not exist in the list')


csll = CircularDoublyLinkedList()



csll.creation('a')
csll.insertion('b',1)
print('c')
# print([node.value for node in csll])

csll.insertion('c',2)
print([node.value for node in csll])

csll.insertion('d',3)
csll.insertion('e',-1)
# csll.insertion('fox',-1)
# csll.insertion('cat',2)
# csll.insertion('over',csll.length)
# csll.insertion('jumped',csll.length)
print([node.value for node in csll])

csll.forwardTraverse()
# csll.backWardTraverse()
# csll.searching('a')

# csll.deletion(0)
# print('after head delete')
# csll.forwardTraverse()

# csll.deletion(-1)
# print('after tail delete')
# csll.forwardTraverse()

csll.deletion(2)
print('after index 2 delete')
csll.forwardTraverse()

csll.deletion(0)
print(csll.head.value, 'tailvalue', csll.tail.value)

csll.deletion(-1)

print(csll.head.value, 'tailvalue ', csll.tail.value)
print('tail',csll.tail.value)
csll.deletion(4)
print('taillll',csll.tail.value)
print(csll.head.value, 'tailvalue ', csll.tail.value)

# csll.deletion(7)
# print('after tail index 7 delete')
csll.forwardTraverse()

print(csll.tail.value)

print([node.value for node in csll])
