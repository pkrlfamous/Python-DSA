class Node:
    pass

class LinkedList:
    
    head = None
    def insertAtBeginning(self,new_data):

        node = Node() # create a new node
        node.data = new_data
        node.next = self.head # next for new node becomes the current head
        self.head = node

linkedList = LinkedList()
# linkedList.head = None
linkedList.insertAtBeginning('a')
linkedList.insertAtBeginning('b')
linkedList.insertAtBeginning('c')

print(linkedList.head.next.next.next)