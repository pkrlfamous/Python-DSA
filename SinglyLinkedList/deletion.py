from copy import deepcopy
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.next

    
    def insertIntoList(self, value, position):

        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if position == 0:
                newNode.next = self.head
                self.head = newNode
            elif position == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                node = self.head
                index = 0
                while node and index < position -1:
                    node = node.next
                    index += 1
                newNode.next = node.next
                node.next = newNode

                if self.tail == node:
                    self.tail = newNode
        

    
    def traverse(self):
        node = self.head
        if node is None:
            print('Empty list')
            return
        while(node):
            print(node.value)
            node = node.next

    def search(self, value):
        count = 0
        node = self.head
        found = False
        if node is None:
            print('Empty list')
            return
        
        while(node):
            count += 1
            if node.value == value:
              found = True
              break
            else:  
                node = node.next
        
        if not found:
            print(f"{value} not found.")
        else:
            print(f"{value} found in {count} position.")

    # def delete(self,value):
    #     node = self.head
    #     prev = None
    #     if node is None:
    #         print("Empty list")
    #         return
    #     elif self.head.value == value:
    #         self.head = self.head.next
    #     else:
    #         while(node):
    #             print(node.value,'node value')
    #             if node.value == value:
    #                 break
    #             else:
    #                 prev = node
    #                 node = node.next
    #     print('here',prev.value, node.value)
    #     prev.next = node.next

    #     if self.tail == node:
    #         prev.next = None
    #         self.tail = prev
        
    def delete(self,location):

        if self.head is None:
            print("the linked list doesn't exits")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                node = self.head
                index = 0
                while node and index < location - 1:
                    node = node.next
                    index += 1
                if self.tail == node.next:
                    self.tail = node
                else:
                    node.next = node.next.next
    
    def del_entire_sll(self):
        if self.head is None:
            print("The linked list doestn't exist")
        else:
            self.head = None
            self.tail = None


sll = SinglyLinkedList()

sll.insertIntoList(1,0)
sll.insertIntoList(2,-1)
sll.insertIntoList(4,2)
sll.insertIntoList(3,2)
# sll.traverse()
print([node.value for node in sll])
sll.search(16)
sll.delete(3)
print(sll.tail.value)
print([node.value for node in sll])






                