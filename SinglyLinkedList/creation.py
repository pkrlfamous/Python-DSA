class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    

    def insertSinglyLinkedList(self, value, position):

        newnode = Node(value)

        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            if position == 0:
                newnode.next = self.head
                self.head = newnode
            elif position == -1:
                self.tail.next = newnode
                self.tail = newnode
            else:
                index = 0
                tempnode = self.head
                while index < position - 1 and tempnode:
                    tempnode = tempnode.next
                    index += 1
                
                if not tempnode:
                    self.tail.next = newnode
                    self.tail = newnode
                    return
                newnode.next = tempnode.next
                tempnode.next = newnode
                if tempnode == self.tail:
                    self.tail = newnode
                # nextNode = tempNode.next
                # tempNode.next = newnode
                # newnode.next = nextNode
                # if tempNode == self.tail:
                #     self.tail = newnode
    
    def printVal(self):
        values = []
        node = self.head
        print('here',node.value)
        while node:
            values.append(node.value)
            node = node.next
        print(values)

singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insertSinglyLinkedList(1, 1)                   
singlyLinkedList.insertSinglyLinkedList(2, 1)                   
singlyLinkedList.insertSinglyLinkedList(3, 2)                   
singlyLinkedList.insertSinglyLinkedList(5, 3)                   
singlyLinkedList.insertSinglyLinkedList(4, 3)                   
singlyLinkedList.insertSinglyLinkedList(8, -1)                   
singlyLinkedList.insertSinglyLinkedList(7, 5)                   
singlyLinkedList.insertSinglyLinkedList(6, 5)                   
singlyLinkedList.insertSinglyLinkedList(20, -1)                   
# singlyLinkedList.printVal()

# what does iter do? the iter allows to loop over the         

print([node.value for node in singlyLinkedList])
