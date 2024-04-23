class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyDoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("insert error: index out of range.")
            return
        if index == 0:
            self.prepend(value)
            return

        new_node = Node(value)

        leader = self.traverse_to_index(index - 1)
        follower = leader.next

        leader.next = new_node
        new_node.prev = leader
        new_node.next = follower
        follower.prev = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length:
            print("remove error: index out of range.")
            return
        if index == 0:
            self.head = self.head.next
            return

        last_node = self.traverse_to_index(index - 1)
        removed_node = last_node.next
        next_node = removed_node.next
        next_node.prev = last_node

        last_node.next = removed_node.next
        self.length -= 1

    def traverse_to_index(self, index):
        last_node = self.head
        count = 0

        while count != index:
            last_node = last_node.next
            count += 1

        return last_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")


if __name__ == "__main__":
    my_doublylinkedlist = MyDoublyLinkedList(6)
    my_doublylinkedlist.append(1)
    my_doublylinkedlist.append(5)
    my_doublylinkedlist.print_list()
    my_doublylinkedlist.prepend(7)
    my_doublylinkedlist.prepend(2)
    my_doublylinkedlist.print_list()
    print("insert 10 in position 2")
    my_doublylinkedlist.insert(2, 10)
    my_doublylinkedlist.print_list()
    print("insert 20 in position 4")
    my_doublylinkedlist.insert(4, 20)
    my_doublylinkedlist.print_list()
    print("remove in position 2")
    my_doublylinkedlist.remove(2)
    my_doublylinkedlist.print_list()
    print("remove in position 4")
    my_doublylinkedlist.remove(4)
    my_doublylinkedlist.print_list()

