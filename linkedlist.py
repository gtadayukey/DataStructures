class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
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
        temp = leader.next

        leader.next = new_node
        new_node.next = temp
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
    my_linkedlist = MyLinkedList(6)
    my_linkedlist.append(1)
    my_linkedlist.append(5)
    my_linkedlist.prepend(7)
    my_linkedlist.prepend(2)
    my_linkedlist.print_list()
    print("insert 10 in position 2")
    my_linkedlist.insert(2, 10)
    my_linkedlist.print_list()
    print("insert 20 in position 4")
    my_linkedlist.insert(4, 20)
    my_linkedlist.print_list()
    print("remove in position 2")
    my_linkedlist.remove(2)
    my_linkedlist.print_list()
    print("remove in position 4")
    my_linkedlist.remove(4)
    my_linkedlist.print_list()

