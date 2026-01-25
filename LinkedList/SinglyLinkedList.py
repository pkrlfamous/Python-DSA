import time
class Node:
    def __init__(self, data):
        self.data = data # Assigns the given data to the node
        self.next = None # Initialize the next attribute to null

class MiddleNode:
    def __init__(self,oldData, newData):
        self.oldData = oldData
        self.newData = newData

class LinkedList:
    # def __init__(self):
    #     self.head = None # initialize head as None
    
    head = None
    def insertAtBeginning(self,new_data):

        new_node = Node(new_data) # create a new node
        new_node.next = self.head # next for new node becomes the current head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    """
    intuition
    first create a node to be inserted
    First if head.next is None, head = node
    loop until the next node is None. and assign temp = temp.next

    if None come out of the loop and assign the next to the new node.
    """

    def insertAtEnd(self, new_data):
        node = Node(new_data)
        if self.head == None:
            self.head = node
            return
        
        temp = self.head
        while temp.next:
            # print('temp',temp.data)
            temp = temp.next
        temp.next = node
    
    def insertAtMiddle(self, oldData, newData):
        node = MiddleNode(oldData, newData)
        temp = self.head
        # print(temp.data)
        print('inside insertMiddle')
        linkedList.printList()
        while node.oldData != temp.data:
            print(temp.data)
            temp = temp.next
            # time.sleep(1)
        
        newNode = Node(newData)
        rightNode = temp.next
        temp.next = newNode
        newNode.next = rightNode
        print("-"*80)
    
    # deleting a node from the beginning of a linked list
    def deleteHeadNode(self):
        if self.head == None:
            return
        
        temp = self.head.next
        self.head = temp


    # deleting a node from the end of a linked list
    def deleteFromEnd(self):
        if self.head is None:
            return 'List is empty'
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        
        temp.next = None

    # searching a linked list for a specific value

    def searchValue(self, value):
        if self.head is None:
            return 'List is empty'

        temp = self.head
        counter = 0
        while(temp):
            print(temp.data, value)
            if temp.data == value:
                counter += 1
                break
            else:
                temp = temp.next
                counter += 1
        if counter>0:
            print('found in',counter,'place')
            return counter
        else:
            print('value not found')


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insertAtBeginning('quick')
    linkedList.insertAtBeginning('a')
    linkedList.printList()
    linkedList.insertAtEnd('fox')
    linkedList.insertAtMiddle('quick','brown')
    linkedList.printList()
    linkedList.insertAtMiddle('fox','jumped')
    linkedList.printList()
    linkedList.deleteHeadNode()
    linkedList.printList()
    print('delete from end')
    linkedList.deleteFromEnd()
    linkedList.printList()
    linkedList.searchValue("fox")





linkedList.printList()


