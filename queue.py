class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if not self.first:
            return print("nothing to see here..")
        return print(self.first.value)

    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.first is None:
            return print("nothing to pop here..")
        if self.last == self.first:
            self.last = None

        self.first = self.first.next
        self.length -= 1

    def print_queue(self):
        current_node = self.first
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")


if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.enqueue("Mario")
    my_queue.enqueue("Silas")
    my_queue.enqueue("Pedro")
    my_queue.enqueue("José")
    my_queue.enqueue("Carlos")
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.print_queue()
    my_queue.peek()
