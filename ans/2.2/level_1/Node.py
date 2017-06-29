class Node:
    def __init__(self, element):
        self.element = element
        self.next    = None
        self.prev    = None

    def getElement(self):
        return self.element

    def getNext(self):
        return self.next

    def setNext(self, Node):
        self.next = Node

    def getPrev(self):
        return self.prev

    def setPrev(self, Node):
        self.prev = Node

    def __del__(self):
        return self.element
