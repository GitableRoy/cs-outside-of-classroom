from __future__ import print_function

class Array:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size

    def insert(self, index, element):
        if not 0 <= index <= (self.size - 1):
            return
        else:
            self.array[index] = element

    def prepend(self, element):
        self.array[0] = element

    def append(self, element):
        self.array[self.size - 1] = element

    def get(self, index):
        if not type(index) == type(0):
            return
        elif not 0 <= index <= (self.size - 1):
            return
        else:
            return self.array[index]

    def front(self):
        return self.array[0]

    def back(self):
        return self.array[(self.size - 1)]

    def search(self, element):
        for index in range(0, (self.size - 1)):
            if self.array[index] == element:
                return index

    def remove(self, index):
        if not type(index) == type(0):
            return
        elif not 0 <= index <= (self.size - 1):
            return
        else:
            self.array[index] = None

    def popFront(self):
        element = self.array[0]
        self.array[0] = None
        return element

    def popBack(self):
        element = self.array[(self.size-1)]
        self.array[self.size-1] = None
        return element

    def getSize(self):
        return self.size

    def printArray(self):
        for index in range(0, self.size):
            print(str(self.array[index])+" ", end=" ")
        print()
