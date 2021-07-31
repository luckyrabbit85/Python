class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            return "EMPTY"
        else:
            temp = self.head
            while temp:
                print(temp.value, "->", end=" ")
                temp = temp.next


singlyLinkedList = SLinkedList()

print(singlyLinkedList.head)
print(singlyLinkedList.tail)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

print("\n")
print(node1)
print(node2)
print(node3)


singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.head.next.next = node3
singlyLinkedList.tail = node3

print("\n")
print(singlyLinkedList.head)
print(singlyLinkedList.tail)

print("\n")
print(singlyLinkedList.head.value)
print(singlyLinkedList.head.next.value)
print(singlyLinkedList.head.next.next.value)

print("\n")
singlyLinkedList.display()
