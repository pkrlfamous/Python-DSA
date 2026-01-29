class Node:
    def __init__(self, value):
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

    def creation(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    def insertIntoList(self, value, position):
        new_node = Node(value)

        if self.head is None:
            print("The node cannot be inserted.")
            return

        if position == 0:
            self._insert_at_head(new_node)
        elif position == -1:
            self._insert_at_tail(new_node)
        else:
            self._insert_at_position(new_node, position)

    def _insert_at_head(self,node):
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def _insert_at_tail(self,node):
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    
    def _insert_at_position(self,node,position):
        current = self.head
        index = 0

        while current and index < position -1:
            current = current.next
            index += 1
        
        if self.tail == current or current is None:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            # or self._insert_at_tail(node)
        else:
            node.prev = current
            node.next = current.next
            current.next.prev = node
            current.next = node

    def traverse(self):
        node = self.head
        if self.head is None:
            print("list is empty")
            return
        elements = []
        while node:
            elements.append(str(node.value))
            node = node.next
        
        print(" <-> ".join(elements) + " -> None")
        print(f"Head: {self.head.value}, Tail: {self.tail.value}")
    
    def reverseTraverse(self):
        node = self.tail
        if not node:
            print("Empty list")
            return
        elements = []
        while node:
            elements.append(str(node.value))
            node = node.prev
        
        print(" <-> ".join(elements) + " -> None")
        print(f"Head: {self.head.value} Tail: {self.tail.value}")

    def search(self,value):
        if self.head is None:
            print("Empty list")
            return
        node = self.head
        found = False
        count = 0
        while node:
            count += 1
            if value == node.value:
                found = True
                break
            else:
                node = node.next
        
        if found:
            print(f"{value} found at location {count}")
        else:
            print("Value not found")

    def deletion(self, position):
        
        if self.head is None:
            print("Empty list")
            return

        if position == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        
        if position == -1:
            if self.head == self.tail:
                self.head, self.tail = None, None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        

        # delete at specific position
        current = self.head
        count = 0
        # traverse to the node just before the one we want to delete
        while current and count < position - 1:
            current = current.next
            count += 1
        
        # validation
        # 1. current is None: we ran past the end of the list
        # 2. current.next is None: we are at the tail, so there is no "next" node to delete (index out of bounds)
        if current is None or current.next is None:
            print("Index out of range")
            return
        
        node_to_delete = self.tail
        # special if the node to delete is actually the tail
        if node_to_delete == self.tail:
            self.tail = current
            current.next = None
        else:
            # standar middle deletion
            current.next = node_to_delete.next
            # check if the new next exists before accssing .prev
            if current.next:
                current.next.prev = current


dll = DoublyLinkedList()

dll.creation(0)
dll.insertIntoList(1,1)
dll.insertIntoList(2,2)
dll.insertIntoList(4,3)
dll.insertIntoList(3,3)

print([node.value for node in dll])
dll.traverse()
dll.reverseTraverse()
dll.search(4)
dll.insertIntoList(5,5)
print('after insertion tail',dll.tail.value)
dll.traverse()
dll.deletion(4)
dll.traverse()
print('taillll',dll.tail.value)
dll.deletion(4)

dll.traverse()
