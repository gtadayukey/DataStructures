class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyStack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if not self.top:
            return print("nothing to see here..")
        return print(self.top.value)

    def push(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer

        self.length += 1

    def pop(self):
        if self.bottom is None:
            return print("nothing to pop here..")
        if self.bottom == self.top:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1

    def print_stack(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")


if __name__ == "__main__":
    my_stack = MyStack()
    my_stack.push(4)
    my_stack.push(3)
    my_stack.push(1)
    my_stack.print_stack()
    my_stack.pop()
    my_stack.print_stack()
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
    my_stack.print_stack()
    my_stack.pop()
    my_stack.pop()




