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

        while node:
            yield node
            node = node.next
    

    def insertIntoList(self, value, position):
        newnode = Node(value)

        if self.head is None:
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
                tempnode = self.head
                index = 0

                while tempnode.next and index < position - 1:
                    tempnode = tempnode.next
                    index += 1 
                newnode.next = tempnode.next
                tempnode.next = newnode
                if tempnode == self.tail:
                    self.tail = newnode

    def traverse(self):
        node = self.head
        if not node:
            return
        else:
            while node:
                print(node.value)
                node = node.next
    
    def search(self, value):
        node = self.head
        count = 0

        if self.head is None:
            print('empty list')
            return
        else:
            while node.next is not None:
                count += 1
                if node.value == value:
                    break
                else:
                    node = node.next
        print(f"Result: {count if count > 0 else 'not found'}")

sll = SinglyLinkedList()

sll.insertIntoList(1,0)

sll.insertIntoList(2,-1)
sll.insertIntoList(3,10)
sll.insertIntoList(4,4)

print([node.value for node in sll])
sll.search(2)

# sll.traverse()
