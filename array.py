class MyArray:
    def __init__(self):
        self._length = 0
        self._data = []

    @property
    def data(self):
        return self._data

    def get(self, index):
        if 0 <= index < self._length:
            return self._data[index]

        return IndexError("Index out of range")

    def push(self, item):
        self._data.append(item)
        self._length += 1

    def pop(self):
        if self._length == 0:
            return IndexError("Array is empty")

        self._length -= 1
        del self._data[self._length]

    def delete(self, index):
        if 0 <= index < self._length:
            i = index

            while i < self._length - 1:
                self._data[i] = self._data[i + 1]
                i += 1

            del self._data[self._length - 1]
            self._length -= 1

        else:
            return IndexError("Index out of range")


if __name__ == "__main__":
    my_array = MyArray()

    my_array.push("apple")
    my_array.push("orange")
    my_array.push("banana")
    print("Array after push:", my_array.data)

    print("Element in position 1:", my_array.get(1))

    my_array.pop()
    print("Array after pop:", my_array.data)

    my_array.delete(0)
    print("Array after delete:", my_array.data)
