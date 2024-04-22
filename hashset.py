def _hash(key):
    hashcode = i = 0
    while i < len(key):
        hashcode = (hashcode + ord(key[i]) * i)
        i += 1
    return hashcode


class MyHashSet:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        address = _hash(key)
        if address not in self.data:
            self.data[address] = []
            self.data[address].append([key, value])

    def get(self, key):
        address = _hash(key)
        if address not in self.data:
            return None
        current = self.data[address]
        i = 0
        while i < len(current):
            if current[i][0] == key:
                return current[i][1]
            i += 1

    def keys(self):
        key_list = []
        for pair in self.data.values():
            for key, _ in pair:
                key_list.append(key)
        return key_list


if __name__ == "__main__":
    my_hashset = MyHashSet()
    my_hashset.set('grapes', 10000)
    my_hashset.set('orange', 520)
    my_hashset.set('pineapple', 20)
    my_hashset.set('banana', 300)
    my_hashset.set('lime', 120)
    print(my_hashset.get('pineapple'))
    print(my_hashset.get('grapes'))
    print(my_hashset.get('lime'))
    print(my_hashset.keys())

