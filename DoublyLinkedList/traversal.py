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

dll = DoublyLinkedList()

dll.creation(0)
dll.insertIntoList(1,1)
dll.insertIntoList(2,2)
dll.insertIntoList(4,3)
dll.insertIntoList(3,3)

print([node.value for node in dll])
dll.traverse()