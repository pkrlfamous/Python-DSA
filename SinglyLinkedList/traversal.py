class Node:

    def __init__(self, data):
        self.data = data
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

    def insertIntoList(self, data, position):
        newnode = Node(data)

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
                tempnode = self.head
                index = 0
                while index < position-1 and tempnode:
                    tempnode = tempnode.next
                    index += 1
                newnode.next = tempnode.next
                tempnode.next = newnode

    def traverse(self):
        node = self.head
        if not node:
            print('Empty list')
            return
        while node:
            print(node.data)
            node = node.next


sll = SinglyLinkedList()
sll.insertIntoList("A", 0)
sll.insertIntoList("quick", -1)
sll.insertIntoList("jumped", -1)
sll.insertIntoList("fox", 2)
sll.insertIntoList("over", -1)
sll.insertIntoList("a", -1)

sll.traverse()
