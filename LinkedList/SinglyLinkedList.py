class Node:
    def __init__(self, data):
        self.data = data # Assigns the given data to the node
        self.next = None # Initialize the next attribute to null

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
    

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insertAtBeginning('fox')
    linkedList.insertAtBeginning('brown')
    linkedList.insertAtBeginning('quick')
    linkedList.insertAtBeginning('a')

linkedList.printList()


